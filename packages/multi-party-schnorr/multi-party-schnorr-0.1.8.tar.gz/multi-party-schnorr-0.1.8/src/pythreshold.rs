use crate::pykeypair::*;
use crate::pyo3utils::*;
use curv::cryptographic_primitives::commitments::hash_commitment::HashCommitment;
use curv::cryptographic_primitives::commitments::traits::Commitment;
use curv::elliptic::curves::traits::{ECPoint, ECScalar};
use curv::cryptographic_primitives::secret_sharing::feldman_vss::{VerifiableSS,ShamirSecretSharing};
use curv::cryptographic_primitives::hashing::traits::Hash;
use curv::arithmetic::traits::Samplable;
use curv::{BigInt, FE, GE};
use pyo3::prelude::*;
use pyo3::exceptions::ValueError;
use pyo3::types::{PyBytes,PyList,PyTuple,PyType};
use curv::cryptographic_primitives::hashing::hash_sha256::HSha256;
use threadpool::ThreadPool;
use std::sync::mpsc::channel;


#[pyclass]
pub struct PyThresholdKey {
    #[pyo3(get)]
    pub keypair: PyKeyPair,
    #[pyo3(get)]
    pub my_index: Option<usize>,
    #[pyo3(get)]
    pub parties_index: Vec<usize>,
    #[pyo3(get)]
    pub t: usize, // threshold
    #[pyo3(get)]
    pub n: usize,
}

#[pymethods]
impl PyThresholdKey {
    #[classmethod]
    fn generate(_cls: &PyType, _py: Python, t: usize, n: usize, parties_index: Option<&PyList>)
        -> PyResult<PyThresholdKey> {
        if t >= n {
            return Err(ValueError::py_err("require \"t < n\""));
        };
        let parties_index = pylist2parties_index(_py, n, parties_index)?;
        let my_index = None;  // unknown at this point
        let keypair = generate_keypair(_py);
        {
            // commitment check
            let blind_factor = BigInt::sample(256);
            let commitment = HashCommitment::create_commitment_with_user_defined_randomness(
                &keypair.public.bytes_compressed_to_big_int(),
                &blind_factor,
            );  // com = bc1 of KeyGenBroadcastMessage1
            let h = HashCommitment::create_commitment_with_user_defined_randomness(
                    &keypair.public.bytes_compressed_to_big_int(), &blind_factor);
            if h != commitment {
                return Err(ValueError::py_err("test commitment check failed"));
            }
        }
        //obj.init(PyThresholdKey { keypair, my_index, parties_index, t, n});
        Ok(PyThresholdKey { keypair, my_index, parties_index, t, n})
    }

    #[classmethod]
    fn from_secret_key(_cls: &PyType, _py: Python, t: usize, n: usize, secret: &PyBytes, my_index: usize, parties_index: Option<&PyList>)
        -> PyResult<PyThresholdKey> {
        if t >= n {
            return Err(ValueError::py_err("require \"t < n\""));
        };
        let ec_point: GE = ECPoint::generator();
        let secret: FE = ECScalar::from(&BigInt::from(secret.as_bytes()));
        let public: GE = ec_point.scalar_mul(&secret.get_element());
        let keypair = PyKeyPair {secret, public};
        let parties_index = pylist2parties_index(_py, n, parties_index)?;
        let my_index = Some(my_index);
        Ok(PyThresholdKey { keypair, my_index, parties_index, t, n})
    }

    fn get_commitment(&self, _py: Python) -> PyObject {
        let blind_factor = BigInt::sample(256);
        let commitment = HashCommitment::create_commitment_with_user_defined_randomness(
            &self.keypair.public.bytes_compressed_to_big_int(),
            &blind_factor,
        );  // com = bc1 of KeyGenBroadcastMessage1
        let blind_factor = bigint2bytes(&blind_factor).unwrap();
        let commitment = bigint2bytes(&commitment).unwrap();
        PyTuple::new(_py, &[
            PyBytes::new(_py, &blind_factor),
            PyBytes::new(_py, &commitment),
        ]).to_object(_py)
    }

    fn get_variable_secret_sharing(&self, _py: Python) -> PyResult<PyObject> {
        // index users [0, 1, .., n] => [1, 2, ...,n+1]
        let (vss_scheme, secret_shares) = VerifiableSS::share_at_indices(
                self.t, self.n, &self.keypair.secret, &self.parties_index);

        let vss_point: Vec<&PyBytes> = vss_scheme.commitments.iter()
            .map(|com| PyBytes::new(_py, &com.get_element().serialize_compressed()))
            .collect();
        let secret_scalar: Vec<&PyBytes> = secret_shares.iter()
            .map(|int| PyBytes::new(_py, &bigint2bytes(&int.to_big_int()).unwrap()))
            .collect();
        Ok(PyTuple::new(_py, &[
            PyTuple::new(_py, &vss_point),
            PyTuple::new(_py, &secret_scalar),
        ]).to_object(_py))
    }

    fn keygen_t_n_parties(&mut self, _py: Python, signers: &PyList, vss_points: &PyList, secret_scalars: &PyList)
        -> PyResult<PyObject> {
        if self.n != signers.len() {
            return Err(ValueError::py_err("not correct signers length"));
        } else if self.n != vss_points.len() {
            return Err(ValueError::py_err("not correct vss_points length"));
        } else if self.n != secret_scalars.len() {
            return Err(ValueError::py_err("not correct secret_scalars length"));
        }

        // convert python type => Rust type
        let signers = pylist2points(signers)?;  // = y_vec
        let vss_scheme_vec = {
            let vss_points: Vec<Vec<Vec<u8>>> = vss_points.extract()?;
            let mut tmp = Vec::with_capacity(vss_points.len());
            for vss in vss_points {
                let mut points = Vec::with_capacity(vss.len());
                for p in vss {
                    let p = bytes2point(p.as_slice())?;
                    points.push(p);
                }
                tmp.push(VerifiableSS {
                    parameters: ShamirSecretSharing {
                        threshold: self.t, share_count: self.n
                    },
                    commitments: points
                });
            };
            tmp
        };
        let secret_shares_vec = {
            let secret_scalars: Vec<Vec<Vec<u8>>> = secret_scalars.extract()?;
            let mut tmp = Vec::with_capacity(secret_scalars.len());
            for lists in secret_scalars {
                let mut inner = Vec::with_capacity(lists.len());
                for scalar in lists {
                    let s: FE = ECScalar::from(&BigInt::from(scalar.as_slice()));
                    inner.push(s);
                };
                tmp.push(inner);
            };
            tmp
        };

        // your index
        let my_index = match self.my_index {
            Some(i) => i,
            None => {
                let mut my_index: Option<usize> = None;
                for (index, signer) in signers.iter().enumerate() {
                    if signer == &self.keypair.public {
                        my_index = Some(index);
                        break;
                    }
                }
                if my_index.is_none() {
                    return Err(ValueError::py_err("cannot find your position"));
                }
                my_index.unwrap()
            }
        };

        // calculate party share
        let mut party_share = Vec::with_capacity(self.n);
        for i in 0..self.n {
            let party = match secret_shares_vec[i].get(my_index) {
                Some(scalar) => scalar.clone(),
                None => return Err(ValueError::py_err("not found your index on secret_shares"))
            };
            party_share.push(party);
        }

        // calculate party_share sum
        let x_i = party_share.iter().fold(FE::zero(), |acc, x| acc + x);
        let x_i = bigint2bytes(&x_i.to_big_int()).expect("too large x_i");

        // verify vss construct keypair
        {
            let pool = ThreadPool::new(num_cpus::get());
            let (tx, rx) = channel();
            for i in 0..self.n {
                let vss_scheme = vss_scheme_vec[i].to_owned();
                let share_point = party_share[i].to_owned();
                let position = self.parties_index[my_index].to_owned();
                let public_key = signers[i].to_owned();
                let tx = tx.clone();
                pool.execute(move || {
                    if vss_scheme.validate_share(&share_point, position).is_err() {
                        tx.send(Err(format!("failed vss validation check: idx={}", i)));
                    } else if vss_scheme.commitments[0] != public_key {
                        tx.send(Err(format!("failed vss commitment signer check: idx={}", i)));
                    } else {
                        tx.send(Ok(()));
                    }
                });
            };

            // wait for all jobs finish
            let n = self.n.to_owned();
            let exception = _py.allow_threads(move || {
                for result in rx.iter().take(n) {
                    if result.is_err() {
                        return Err(result.unwrap_err())
                    }
                }
                Ok(())
            });
            exception.map_err(|err| {
                ValueError::py_err(err)
            })?;
        }
        // success generate sharedKey
        self.my_index = Some(my_index);
        Ok(PyBytes::new(_py, &x_i).to_object(_py))
    }
}

pub fn sum_public_points(signers: &Vec<GE>) -> PyResult<GE> {
    // return Y params of sharedKey
    // return V params of eph sharedKey
    if signers.len() < 1 {
        return Err(ValueError::py_err("zero length point isn't allowed"));
    }
    let mut signers = signers.iter();
    let head = signers.next().unwrap();
    let sum = signers.fold(head.clone(), |acc, x| acc + x);
    Ok(sum)
}

pub fn compute_local_signature(share: &FE, eph_share: &FE, Y: &GE, V: &GE, message: &[u8]) -> (FE, FE) {
    // each party computes and share a local sig
    let beta_i = eph_share.clone();
    let alpha_i = share.clone();

    let e_bn = HSha256::create_hash(&[
            &V.bytes_compressed_to_big_int(),
            &Y.bytes_compressed_to_big_int(),
            &BigInt::from(message),
    ]);
    let e: FE = ECScalar::from(&e_bn);
    let gamma_i = beta_i + e.clone() * alpha_i;
    (e, gamma_i)
}

pub fn sum_local_signature(
    t: usize, e: &FE, gammmas: &Vec<FE>, parties_index: &Vec<usize>,
    vss_points: &Vec<VerifiableSS>, eph_vss_points: &Vec<VerifiableSS>)
    -> Result<FE, String> {
    if vss_points.len() < 1 {
        return Err(String::from("zero length vss_points isn't allowed"));
    } else if eph_vss_points.len() < 1 {
        return Err(String::from("zero length eph_vss_points isn't allowed"));
    } else if gammmas.len() != eph_vss_points[0].parameters.share_count {
        return Err(String::from("not correct gammmas length"));
    }else if parties_index.len() != eph_vss_points[0].parameters.share_count {
        return Err(String::from("not correct parties_index length"));
    } else if t != vss_points[0].parameters.threshold {
        return Err(String::from("not correct vss threshold"));
    } else if vss_points.len() != vss_points[0].parameters.share_count {
        return Err(String::from("not correct vss length"));
    } else if t != eph_vss_points[0].parameters.threshold {
        return Err(String::from("not correct eph_vss threshold"));
    } else if eph_vss_points.len() != eph_vss_points[0].parameters.share_count {
        return Err(String::from("not correct eph_vss length"));
    }
    // n' = num of signers, n - num of parties in keygen
    let comm_vec = (0..t + 1)
        .map(|i| {
            let mut key_gen_comm_i_vec = vss_points.iter()
                .map(|v| v.commitments[i].clone() * e)
                .collect::<Vec<GE>>();
            let mut eph_comm_i_vec = eph_vss_points.iter()
                .map(|v| v.commitments[i].clone())
                .collect::<Vec<GE>>();
            key_gen_comm_i_vec.append(&mut eph_comm_i_vec);
            let mut comm_i_vec_iter = key_gen_comm_i_vec.iter();
            let comm_i_0 = comm_i_vec_iter.next().unwrap();
            comm_i_vec_iter.fold(comm_i_0.clone(), |acc, x| acc + x)
        })
        .collect::<Vec<GE>>();

    let vss_sum = VerifiableSS {
        parameters: eph_vss_points[0].parameters.clone(),
        commitments: comm_vec,
    };

    // validate share public
    let g: GE = GE::generator();
    for (position, gamma) in parties_index.iter().zip(gammmas.iter()) {
        let gamma_i_g = &g * gamma;
        let comm_to_point = vss_sum.get_point_commitment(position + 1);
        if gamma_i_g != comm_to_point {
            return Err(String::from("validate share public failed idx"));
        }
    }
    // each party / dealer can generate the signature
    let gamma_vec = (0..parties_index.len())
        .map(|i| gammmas[i].clone())
        .collect::<Vec<FE>>();
    let reconstruct_limit = vss_sum.parameters.threshold.clone() + 1;
    let sigma = vss_sum.reconstruct(
        &parties_index[0..reconstruct_limit.clone()],
        &gamma_vec[0..reconstruct_limit.clone()],
    );
    Ok(sigma)
}


pub fn verify_threshold_signature(sigma: FE, Y: &GE, V: &GE, message: &[u8]) -> bool {
    let e_bn = HSha256::create_hash(&[
        &V.bytes_compressed_to_big_int(),
        &Y.bytes_compressed_to_big_int(),
        &BigInt::from(message),
    ]);
    let e: FE = ECScalar::from(&e_bn);

    let g: GE = GE::generator();
    let sigma_g = g * &sigma;
    let e_y = Y * &e;
    let e_y_plus_v = e_y + V;

    return e_y_plus_v == sigma_g;
}
