use crate::pythreshold::verify_threshold_signature;
use crate::pyagg::verify_aggregate_signature;
use crate::pyo3utils::{decode_public_bytes, PyKeyType, bytes2point_inner};
use curv::elliptic::curves::traits::{ECScalar, ECPoint};
use curv::{BigInt, GE, FE};
use curv::cryptographic_primitives::hashing::hash_sha256::HSha256;
use curv::cryptographic_primitives::hashing::traits::Hash;


#[inline]
pub fn verify_auto_signature(s: &[u8], r: &[u8], apk: &[u8], message: &[u8])
    -> Result<bool, String> {
    let is_verify = match decode_public_bytes(apk) {
        Ok((key_type, _prefix)) => match key_type {
            PyKeyType::SingleSig | PyKeyType::AggregateSig => {
                let signature = BigInt::from(s);
                let r_x = BigInt::from(r);
                let apk = bytes2point_inner(apk)?;
                let is_musig = key_type == PyKeyType::AggregateSig;
                verify_aggregate_signature(&signature, &r_x, &apk, message, is_musig).is_ok()
            },
            PyKeyType::ThresholdSig => {
                let sigma = ECScalar::from(&BigInt::from(s));
                let Y = bytes2point_inner(apk)?;
                let V = bytes2point_inner(r)?;
                verify_threshold_signature(sigma, &Y, &V, message)
            }
        },
        Err(_) => return Err("decode public point failed".to_string())
    };
    Ok(is_verify)
}


pub fn ephemeral_hash_0(r_hat: &GE, apk: &GE, message: &[u8], musig_bit: bool) -> BigInt {
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


pub fn add_scalar_parts(s1: BigInt, s2: &BigInt) -> BigInt {
    if *s2 == BigInt::from(0) {
        s1
    } else {
        let s1_fe: FE = ECScalar::from(&s1);
        let s2_fe: FE = ECScalar::from(&s2);
        let s1_plus_s2 = s1_fe.add(&s2_fe.get_element());
        s1_plus_s2.to_big_int()
    }
}
