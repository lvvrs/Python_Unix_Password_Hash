"""
This script determinating type hash for unix password.
Available hash type's:
1) MD5
2) SHA-256
3) SHA-512

Author: Vladimir Leonov
Release: 0.0.3
Date: 06.01.2022
"""


def determinating_type_hash(pass_hash):
    if pass_hash.startswith('$1'):
        hash_type = 'MD-5'
    elif pass_hash.startswith('$5'):
        hash_type = 'SHA-256'
    elif pass_hash.startswith('$6'):
        hash_type = 'SHA-512'
    else:
        hash_type = 'ERROR Unknown Hash Type or Bad hash!'
    return hash_type
