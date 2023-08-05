#![allow(non_snake_case)]
/*
    Multisig Schnorr

    Copyright 2018 by Kzen Networks

    This file is part of Multisig Schnorr library
    (https://github.com/KZen-networks/multisig-schnorr)

    Multisig Schnorr is free software: you can redistribute
    it and/or modify it under the terms of the GNU General Public
    License as published by the Free Software Foundation, either
    version 3 of the License, or (at your option) any later version.

    @license GPL-3.0+ <https://github.com/KZen-networks/multisig-schnorr/blob/master/LICENSE>
*/

//! aggregated Schnorr {n,n}-Signatures
//!
//! See https://eprint.iacr.org/2018/068.pdf, https://eprint.iacr.org/2018/483.pdf subsection 5.1
use curv::{BigInt, FE, GE};

use curv::cryptographic_primitives::proofs::*;
use curv::elliptic::curves::traits::*;

use curv::cryptographic_primitives::hashing::hash_sha256::HSha256;
use curv::cryptographic_primitives::hashing::traits::*;

use curv::arithmetic::traits::Converter;
use curv::cryptographic_primitives::commitments::hash_commitment::HashCommitment;
use curv::cryptographic_primitives::commitments::traits::*;

#[derive(Debug)]
pub struct KeyPair {
    pub public_key: GE,
    private_key: FE,
}

impl KeyPair {
    pub fn create() -> KeyPair {
        let ec_point: GE = ECPoint::generator();
        let private_key: FE = ECScalar::new_random();
        let public_key = ec_point.scalar_mul(&private_key.get_element());
        KeyPair {
            public_key,
            private_key,
        }
    }

    pub fn create_from_private_key(private_key: &BigInt) -> KeyPair {
        let ec_point: GE = ECPoint::generator();
        let private_key: FE = ECScalar::from(private_key);
        let public_key = ec_point.scalar_mul(&private_key.get_element());
        KeyPair {
            public_key,
            private_key,
        }
    }
}

#[derive(Debug)]
pub struct KeyAgg {
    pub apk: GE,
    pub hash: BigInt,
}

impl KeyAgg {
    pub fn key_aggregation(my_pk: &GE, other_pk: &GE) -> KeyAgg {
        let hash = HSha256::create_hash(&[
            &BigInt::from(1),
            &my_pk.bytes_compressed_to_big_int(),
            &my_pk.bytes_compressed_to_big_int(),
            &other_pk.bytes_compressed_to_big_int(),
        ]);
        let hash_fe: FE = ECScalar::from(&hash);
        let a1 = my_pk.scalar_mul(&hash_fe.get_element());

        let hash2 = HSha256::create_hash(&[
            &BigInt::from(1),
            &other_pk.bytes_compressed_to_big_int(),
            &my_pk.bytes_compressed_to_big_int(),
            &other_pk.bytes_compressed_to_big_int(),
        ]);
        let hash2_fe: FE = ECScalar::from(&hash2);
        let a2 = other_pk.scalar_mul(&hash2_fe.get_element());
        let apk = a2.add_point(&(a1.get_element()));
        KeyAgg { apk, hash }
    }

    pub fn key_aggregation_n(pks: &[GE], party_index: usize) -> KeyAgg {
        let bn_1 = BigInt::from(1);
        let x_coor_vec: Vec<BigInt> = pks
            .iter()
            .map(|pk| pk.bytes_compressed_to_big_int())
            .collect();

        let hash_vec: Vec<BigInt> = x_coor_vec
            .iter()
            .map(|pk| {
                let mut vec = Vec::new();
                vec.push(&bn_1);
                vec.push(pk);
                for mpz in x_coor_vec.iter().take(pks.len()) {
                    vec.push(mpz);
                }
                HSha256::create_hash(&vec)
            })
            .collect();

        let mut apk_vec: Vec<GE> = pks
            .iter()
            .zip(&hash_vec)
            .map(|(pk, hash)| {
                let hash_t: FE = ECScalar::from(&hash);
                let pki: GE = pk.clone();
                pki.scalar_mul(&hash_t.get_element())
            })
            .collect();

        let pk1 = apk_vec.remove(0);
        let sum = apk_vec
            .iter()
            .fold(pk1, |acc, pk| acc.add_point(&pk.get_element()));

        KeyAgg {
            apk: sum,
            hash: hash_vec[party_index].clone(),
        }
    }
}

#[derive(Debug)]
pub struct EphemeralKey {
    pub keypair: KeyPair,
    pub commitment: BigInt,
    pub blind_factor: BigInt,
}

impl EphemeralKey {
    pub fn create() -> EphemeralKey {
        let keypair = KeyPair::create();
        let (commitment, blind_factor) =
            HashCommitment::create_commitment(&keypair.public_key.bytes_compressed_to_big_int());
        EphemeralKey {
            keypair,
            commitment,
            blind_factor,
        }
    }

    pub fn create_from_private_key(x1: &KeyPair, message: &[u8]) -> EphemeralKey {
        let base_point: GE = ECPoint::generator();
        let hash_private_key_message =
            HSha256::create_hash(&[&x1.private_key.to_big_int(), &BigInt::from(message)]);
        let ephemeral_private_key: FE = ECScalar::from(&hash_private_key_message);
        let ephemeral_public_key = base_point.scalar_mul(&ephemeral_private_key.get_element());
        let (commitment, blind_factor) =
            HashCommitment::create_commitment(&ephemeral_public_key.bytes_compressed_to_big_int());
        EphemeralKey {
            keypair: KeyPair {
                public_key: ephemeral_public_key,
                private_key: ephemeral_private_key,
            },
            commitment,
            blind_factor,
        }
    }

    pub fn test_com(r_to_test: &GE, blind_factor: &BigInt, comm: &BigInt) -> bool {
        let computed_comm = &HashCommitment::create_commitment_with_user_defined_randomness(
            &r_to_test.bytes_compressed_to_big_int(),
            blind_factor,
        );
        computed_comm == comm
    }

    pub fn add_ephemeral_pub_keys(r1: &GE, r2: &GE) -> GE {
        r1.add_point(&r2.get_element())
    }

    pub fn hash_0(r_hat: &GE, apk: &GE, message: &[u8], musig_bit: bool) -> BigInt {
        if musig_bit {
            HSha256::create_hash(&[
                &BigInt::from(0),
                &r_hat.x_coor().unwrap(),
                &apk.bytes_compressed_to_big_int(),
                &BigInt::from(message),
            ])
        } else {
            HSha256::create_hash(&[
                &r_hat.x_coor().unwrap(),
                &apk.bytes_compressed_to_big_int(),
                &BigInt::from(message),
            ])
        }
    }

    pub fn sign(r: &EphemeralKey, c: &BigInt, x: &KeyPair, a: &BigInt) -> BigInt {
        let c_fe: FE = ECScalar::from(c);
        let a_fe: FE = ECScalar::from(a);
        let s_fe = r.keypair.private_key.clone() + (c_fe * x.private_key.clone() * a_fe);
        s_fe.to_big_int()
    }

    pub fn add_signature_parts(s1: BigInt, s2: &BigInt, r_tag: &GE) -> (BigInt, BigInt) {
        if *s2 == BigInt::from(0) {
            (r_tag.x_coor().unwrap(), s1)
        } else {
            let s1_fe: FE = ECScalar::from(&s1);
            let s2_fe: FE = ECScalar::from(&s2);
            let s1_plus_s2 = s1_fe.add(&s2_fe.get_element());
            (r_tag.x_coor().unwrap(), s1_plus_s2.to_big_int())
        }
    }
}

pub fn verify(
    signature: &BigInt,
    r_x: &BigInt,
    apk: &GE,
    message: &[u8],
    musig_bit: bool,
) -> Result<(), ProofError> {
    let base_point: GE = ECPoint::generator();

    let c = if musig_bit {
        HSha256::create_hash(&[
            &BigInt::from(0),
            &r_x,
            &apk.bytes_compressed_to_big_int(),
            &BigInt::from(message),
        ])
    } else {
        HSha256::create_hash(&[
            r_x,
            &apk.bytes_compressed_to_big_int(),
            &BigInt::from(message),
        ])
    };

    let signature_fe: FE = ECScalar::from(signature);
    let sG = base_point.scalar_mul(&signature_fe.get_element());
    let c: FE = ECScalar::from(&c);
    let cY = apk.scalar_mul(&c.get_element());
    let sG = sG.sub_point(&cY.get_element());
    if sG.x_coor().unwrap().to_hex() == r_x.to_hex() {
        Ok(())
    } else {
        Err(ProofError)
    }
}

pub fn verify_partial(
    signature: &FE,
    r_x: &BigInt,
    c: &FE,
    a: &FE,
    key_pub: &GE,
) -> Result<(), ProofError> {
    let g: GE = ECPoint::generator();
    let sG = g * signature;
    let cY = key_pub * a * c;
    let sG = sG.sub_point(&cY.get_element());
    if sG.x_coor().unwrap().to_hex() == *r_x.to_hex() {
        Ok(())
    } else {
        Err(ProofError)
    }
}

mod test;
