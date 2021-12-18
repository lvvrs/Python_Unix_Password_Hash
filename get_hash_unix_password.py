"""
This script generate hash for unix password.
Available method's:
1) MD5
2) SHA-256
3) SHA-512

Author: Vladimir Leonov
Release: 0.0.1
Date: 18.12.2021
Documentation: https://docs.python.org/3/library/crypt.html
Lib Repository: https://github.com/python/cpython/blob/3.10/Lib/crypt.py
"""


import crypt

password = "Pass0rd"

hash_md5 = crypt.crypt(password, salt=crypt.METHOD_MD5)

hash_sha256 = crypt.crypt(password, salt=crypt.METHOD_SHA256)

hash_sha512 = crypt.crypt(password, salt=crypt.METHOD_SHA512)

print("=====MD5=====")
print(hash_md5)
print("=====SHA-256=====")
print(hash_sha256)
print("=====SHA-512=====")
print(hash_sha512)