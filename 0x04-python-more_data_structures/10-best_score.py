#!/usr/bin/python3


def best_score(a_dictionary):
    max_val = 0
    if a_dictionary is None or a_dictionary == {}:
        return None
    for i in a_dictionary.items():
        if i[1] >= max_val:
            # print(i[1])
            max_val = i[1]
        if i[0] is None or i[1] is None:
            return None
    key_list = list(a_dictionary.keys())
    val_list = list(a_dictionary.values())
    pos = val_list.index(max_val)
    return key_list[pos]
