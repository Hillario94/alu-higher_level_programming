#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            j = ord(c) - 32
        else:
            j = ord(c)
        print("{:c}".format(j), end="")
    print("")
