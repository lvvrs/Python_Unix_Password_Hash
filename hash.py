"""
This script used scripts get_hash_unix_password.py
and determinating_type_hash_unix password, for run with command line
arguments.

Available arguments:

-d - determinating type hashes
-g - get pass hashes
-t - select hash type (availabel values - md5, sha256, sha512)
-f - file with list input values
-i - interactive input value

Examples:

    1) hash.py -d -i (hash) - interactive determinating 1 hash
    2) hash.py -d -f (file_name) - determinating hashes type in file (file_name)
    3) hash.py -g -i (password) -t (md5|sha256|sha512) - interactive get 1 hash password with select type
    4) hash.py -g -f (file_name) -t (md5|sha256|sha512) - get hashes for passwords in file_name with select type

If using file, file recomended  place near script, answer created file near input file with name:

For type hashes - type_hashes.txt
For passwords - pass_hashes.txt

Values in file, must be separated with using ','
Available method's:
1) MD5
2) SHA-256
3) SHA-512

Author: Vladimir Leonov
Release: 0.0.1
Date: 31.12.2021
"""


from get_hash_unix_password import get_pass_hash
from determinating_type_hash_unix_password import determinating_type_hash
from sys import argv


print("===========Start Work===========")
if argv[1] == "-d" and argv[2] == "-i":
    print(determinating_type_hash(argv[3]))
elif argv[1] == "-d" and argv[2] == "-f":
    inputed_file = argv[3]
    inputed_file_open = open(inputed_file, 'r')
    file_content = inputed_file_open.read()
    inputed_file_open.close()
    list_values = file_content.split(sep=',')
    output_file_name = "type_hashes.txt"
    output_file = open(output_file_name, 'w')
    for i in list_values:
        type_hash = determinating_type_hash(i)
        output_file.write(type_hash + "\n")
    output_file.close()
    print(output_file_name)
elif argv[1] == "-g" and argv[2] == "-i":
    print(get_pass_hash(argv[3], argv[4]))
elif argv[1] == "-g" and argv[2] == "-f":
    inputed_file = argv[3]
    inputed_file_open = open(inputed_file, 'r')
    file_content = inputed_file_open.read()
    inputed_file_open.close()
    list_values = file_content.split(sep=',')
    output_file_name = "pass_hashes.txt"
    output_file = open(output_file_name, 'w')
    for i in list_values:
        pass_hash = get_pass_hash(i)
        output_file.write(pass_hash + "\n")
    output_file.close()
    print(output_file_name)
elif argv[1] == "--help":
    print("""
Available arguments:

    -d - determinating type hashes
    -g - get pass hashes
    -t - select hash type (availabel values - md5, sha256, sha512)
    -f - file with list input values
    -i - interactive input value
    
Examples:

    1) hash.py -d -i (hash) - interactive determinating 1 hash
    2) hash.py -d -f (file_name) - determinating hashes type in file (file_name)
    3) hash.py -g -i (password) -t (md5|sha256|sha512) - interactive get 1 hash password with select type
    4) hash.py -g -f (file_name) -t (md5|sha256|sha512) - get hashes for passwords in file_name with select type
    """)
else:
    print("Error, check argument, or run script with --help!")
print("===========End Work===========")



