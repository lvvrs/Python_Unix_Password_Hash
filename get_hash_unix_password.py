"""
This script generate hash for unix password.
Available method's:
1) MD5
2) SHA-256
3) SHA-512

Author: Vladimir Leonov
Release: 0.0.2
Date: 21.12.2021
Documentation: https://docs.python.org/3/library/crypt.html
Lib Repository: https://github.com/python/cpython/blob/3.10/Lib/crypt.py
"""


import crypt


def get_pass_hash(password, method):
    if method == "md5":
        pass_hash = crypt.crypt(password, salt=crypt.METHOD_MD5)
    elif method == "sha256":
        pass_hash = crypt.crypt(password, salt=crypt.METHOD_SHA256)
    elif method == "sha512":
        pass_hash = crypt.crypt(password, salt=crypt.METHOD_SHA512)
    else:
        pass_hash = "Error, Bad crypt method!"
    return pass_hash


pass_for_crypt = "Pass0rd"

hash_md5 = get_pass_hash(pass_for_crypt, "md5")

hash_sha256 = get_pass_hash(pass_for_crypt, "sha256")

hash_sha512 = get_pass_hash(pass_for_crypt, "sha512")

bad_hash = get_pass_hash(pass_for_crypt, "sha513")

print("=====MD5=====")
print(hash_md5)
print("=====SHA-256=====")
print(hash_sha256)
print("=====SHA-512=====")
print(hash_sha512)
print("=====Bad_Hash=====")
print(bad_hash)
