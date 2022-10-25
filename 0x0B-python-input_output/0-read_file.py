#!/usr/bin/python3
""" function that opens and reads a filename"""


def read_file(filename=""):
    """read_file is a filename that opens and reads a text file """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
    f.close()
