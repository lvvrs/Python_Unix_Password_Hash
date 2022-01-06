"""
This script work with file which inputed value.
File contain values in type:

    value_1
    value_2
    .
    .
    .
    value_n

Script read values and add values in list.
List with values return in main script hash.py

Author: Vladimir Leonov
Release: 0.0.3
Date: 06.01.2022
"""


def input_file(filepath):
    open_file = open(filepath, 'r')
    file_content = open_file.read()
    list_values = file_content.split(sep='\n')
    list_values = list(filter(None, list_values))
    open_file.close()
    return list_values
