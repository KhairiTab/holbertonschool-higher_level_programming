#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord("a") <= ord(c) <= ord("z"):
            c = (ord(c) + (ord("A")- ord("a")))
    print("{}".format(str), end="")
    print("")
