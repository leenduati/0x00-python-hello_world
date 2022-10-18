#!/usr/bin/python3


def text_indentation(text):
    new_list = list(text)
    count = 0
    for i in new_list:
        count = count + 1
        if i in ['.', '?', ':']:
            new_list.insert(count,'\n')
    for j in new_list:
        print(j, end="")
