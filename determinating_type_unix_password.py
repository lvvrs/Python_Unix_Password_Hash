"""
This script determinating type hash for unix password.
Available method's:
1) MD5
2) SHA-256
3) SHA-512

Author: Vladimir Leonov
Release: 0.0.1
Date: 26.12.2021
"""


def determinating_type_hash(pass_hash):
    if pass_hash.startswith('$1'):
        hash_type = 'MD-5'
    elif pass_hash.startswith('$5'):
        hash_type = 'SHA-256'
    elif pass_hash.startswith('$6'):
        hash_type = 'SHA-512'
    else:
        hash_type = 'ERROR Uncnown Hash Type or Bad hash!'
    return hash_type


hash_examples = [
    "$1$Y9xHJ43R$CbYsBzewxUEAkuxjA4bzo0",
    "$1$GTNnPa68$A7xfFclPgBv.6CIq2NdXB.",
    "$1$tJD45nCj$EmyNV1D8v4pqn/rJnzjTC1",
    "$5$XcSrqTrr1So/YUI.$fXTER2cSAiEYIep8Yb.PGBuKc3dc52OJPL.Py0xYxT1",
    "$5$KoV6YxNahBjAskjw$EQUrponNqjnOH7zpVpi3OE71uV/uJAeL.6xekNSjfCD",
    "$5$9Yue3hjI2uWXkcMy$lEbvrM2HJsHOc0PmWn.qu48.G8QQbNsDFFgPbO5y/p.",
    "$6$v1VLIjGVr6MhPdPW$C.gAHfn4JBc26LpGgtpDy388U.zycGHspDpYOK1WoAT9sPpwOj0GEh.99OrbFDVBgmUVkemvrlvxBaR65Jx5W0",
    "$6$KXfDDJzORZBtPxxc$bly03tWI687P4EUSUJ4FhEZ5muSxwCZZEd9wo45yzS1tvm3Z6bnNqQdqNFfxxiQpFKVU7V74cJ//UIIpEqzoJ1",
    "$6$JD3NcrQ4XIO8Vcyk$riqaddqH3I.y49FDV1NicYwpvCnXWBMgSIKHkrkKx.TYDT6hDJGq7U/JjcB2Ey7.u3DfGyfItmMRWFaqZgqCM.",
    "$7$sadsadsa$dsadasd"
]

for i in hash_examples:
    print(determinating_type_hash(i))