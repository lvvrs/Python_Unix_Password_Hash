"""
This unit test check work function input_file.
Test create file with values and remove file after build

Author: Vladimir Leonov
Release: 0.0.1
Date: 01.01.2022
"""


import unittest
from input_file_work import input_file
from os import remove


test_file = 'test_values.txt'
test_values = ['value_1', 'value_2', 'value_3']
test_string = 'value_1\nvalue_2\nvalue_3'
output_file = open(test_file, 'w')
output_file.write(test_string)
output_file.close()


class MyTestCases(unittest.TestCase):
    def test_work_with_file(self):
        self.assertEqual(input_file(test_file), test_values)
        remove(test_file)


if __name__ == '__main__':
    unittest.main()
