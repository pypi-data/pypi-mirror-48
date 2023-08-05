use curv::cryptographic_primitives::secret_sharing::feldman_vss::{VerifiableSS, ShamirSecretSharing};
use curv::elliptic::curves::traits::ECPoint;
use curv::{BigInt,GE,PK};
use curv::arithmetic::traits::Converter;
use pyo3::prelude::*;
use pyo3::exceptions::ValueError;
use pyo3::types::PyList;


/// Points type
#[derive(PartialEq, Debug)]
pub enum PyKeyType {
    SingleSig,
    AggregateSig,
    ThresholdSig
}

/// Bitcoin public key format converter
/// compressed key   : 2 or 3 prefix + X
/// uncompressed key : 4 prefix      + X + Y
pub fn bytes2point(bytes: &[u8]) -> PyResult<GE> {
    let result = bytes2point_inner(bytes);
    result.map_err(|err| ValueError::py_err(err))
}

#[inline]
pub fn bytes2point_inner(bytes: &[u8]) -> Result<GE, String> {
    let len = bytes.len();
    let hex_bytes = hex::encode(bytes);
    match decode_public_bytes(bytes) {
        Ok((key_type, prefix)) => {
            if len == 33 && (prefix == 2 || prefix == 3) {
                let mut bytes = bytes.to_vec();
                match key_type {
                    PyKeyType::SingleSig => (),
                    PyKeyType::AggregateSig => bytes[0] -= 3,
                    PyKeyType::ThresholdSig => bytes[0] -= 6
                }
                let public = PK::from_slice(&bytes).map_err(
                    |_| format!("0 invalid pk point: {}", hex_bytes))?;
                GE::from_bytes(&public.serialize_uncompressed()[1..]).map_err(
                    |_| format!("1 invalid pk point: {}", hex_bytes))
            }else if len == 65 && prefix == 4 {
                GE::from_bytes(&bytes[1..]).map_err(
                    |_| format!("2 invalid pk point: {}", hex_bytes))
            } else {
                Err(format!("unknown type meta info len={} prefix={}", len, prefix))
            }
        },
        Err(_) => Err(format!("invalid format pk: {}", hex_bytes))
    }
}

/// Mpz bigint to 32bytes big endian
pub fn bigint2bytes(int: &BigInt) -> Result<[u8;32], String> {
    let vec = BigInt::to_vec(int);
    if 32 < vec.len() {
        return Err("too large bigint".to_owned());
    }
    let mut bytes = [0u8;32];
    bytes[(32-vec.len())..].copy_from_slice(&vec);
    Ok(bytes)
}

/// return (PyKeyType, normal_prefix)
/// warning: I will add more params
pub fn decode_public_bytes(bytes: &[u8]) -> Result<(PyKeyType, u8), ()> {
    match bytes.get(0) {
        Some(prefix) => {
            if *prefix == 2 || *prefix == 3 || *prefix == 4 {
                Ok((PyKeyType::SingleSig, *prefix))
            } else if *prefix == 5 || *prefix == 6 || *prefix == 7 {
                Ok((PyKeyType::AggregateSig, *prefix - 3))
            } else if *prefix == 8 || *prefix == 9 || *prefix == 10 {
                Ok((PyKeyType::ThresholdSig, *prefix - 6))
            } else {
                Err(())
            }
        },
        None => Err(())
    }
}

pub fn pylist2points(list: &PyList) -> PyResult<Vec<GE>> {
    let points: Vec<Vec<u8>> = list.extract()?;
    let mut tmp = Vec::with_capacity(points.len());
    for p in points {
        let p = bytes2point(p.as_slice())?;
        tmp.push(p);
    }
    Ok(tmp)
}

pub fn pylist2bigint(list: &PyList) -> PyResult<Vec<BigInt>> {
    let bigints: Vec<Vec<u8>> = list.extract()?;
    let mut tmp = Vec::with_capacity(bigints.len());
    for int in bigints {
        let int = BigInt::from(int.as_slice());
        tmp.push(int);
    }
    Ok(tmp)
}

pub fn pylist2vss(t: usize, n: usize, vss_points: &PyList) -> PyResult<Vec<VerifiableSS>> {
    let vss_points: Vec<Vec<Vec<u8>>> = vss_points.extract()?;
    let mut result = Vec::with_capacity(vss_points.len());
    for vss in vss_points {
        let mut inner = Vec::with_capacity(vss.len());
        for point in vss {
            let point = bytes2point(point.as_slice())?;
            inner.push(point);
        }
        result.push(VerifiableSS {
            parameters: ShamirSecretSharing {
                threshold: t,
                share_count: n
            },
            commitments: inner
        });
    }
    Ok(result)
}

pub fn pylist2parties_index(_py: Python, n: usize, parties_index: Option<&PyList>)
    -> PyResult<Vec<usize>> {
    let vec = match parties_index {
        Some(list) => {
            if n != list.len() {
                return Err(ValueError::py_err("not correct parties_index length"));
            }
            let tmp: Vec<usize> = list.extract()?;
            tmp
        },
        None => (0..n).collect()
    };
    let vec: Vec<usize> = vec.into_iter().map(|i| i + 1).collect();
    Ok(vec)
}
