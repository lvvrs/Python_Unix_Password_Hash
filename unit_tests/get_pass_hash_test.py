"""
This unit test check work function get_pass_hash.
Available method's:
1) MD5
2) SHA-256
3) SHA-512

Author: Vladimir Leonov
Release: 0.0.1
Date: 27.12.2021
"""


import unittest
from get_hash_unix_password import get_pass_hash


class MyTestCases(unittest.TestCase):

    def test_md5_method(self):
        self.assertEqual(get_pass_hash('Password', 'md5')[:2], '$1')

    def test_sha256_method(self):
        self.assertEqual(get_pass_hash('Password', 'sha256')[:2], '$5')

    def test_sha512_method(self):
        self.assertEqual(get_pass_hash('Password', 'sha512')[:2], '$6')

    def test_bad_method(self):
        self.assertEqual(get_pass_hash('Password', 'sha513'), 'Error, Bad crypt method!')


if __name__ == '__main__':
    unittest.main()
