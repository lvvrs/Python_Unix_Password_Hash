"""
This unit test check work function determinating_type_hash.
Available hash type's:
1) MD5
2) SHA-256
3) SHA-512

Author: Vladimir Leonov
Release: 0.0.1
Date: 27.12.2021
"""


import unittest
from determinating_type_hash_unix_password import determinating_type_hash


class TestCases(unittest.TestCase):

    def test_md5_hash(self):
        self.assertEqual(determinating_type_hash('$1$Y9xHJ43R$CbYsBzewxUEAkuxjA4bzo0'), 'MD-5')

    def test_sha256_hash(self):
        self.assertEqual(determinating_type_hash('$5$XcSrqTrr1So/YUI.$fXTER2cSAiEYIep8Yb.PGBuKc3dc52OJPL.Py0xYxT1'),
                         'SHA-256')

    def test_sha512_hash(self):
        self.assertEqual(determinating_type_hash(
          '$6$KXfDDJzORZBtPxxc$bly03tWI687P4EUSUJ4FhEZ5muSxwCZZEd9wo45yzS1tvm3Z6bnNqQdqNFfxxiQpFKVU7V74cJ//UIIpEqzoJ1'),
              'SHA-512')

    def test_error_hash(self):
        self.assertEqual(determinating_type_hash('$7$sadsadsa$dsadasd'), 'ERROR Uncnown Hash Type or Bad hash!')


if __name__ == '__main__':
    unittest.main()
