#!/usr/bin/python3

"""
    function that prints a text with 2 new lines,
     after each of these characters: ., ? and :
"""


def text_indentation(text):
    """This is a function that inputs a newline after ,.:?
    Args:
        text (string): _string value
    Returns:
        text with new_line inserted """

    if type(text) != str:
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1
