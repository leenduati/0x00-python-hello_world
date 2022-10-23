#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if a_dictionary is None or a_dictionary == {}:
        return None
    for i in list(a_dictionary.items()):
        if i[1] == value:
            # print(i[1])
            a_dictionary.pop(i[0])
        continue
        # new_dict.update({i[0]:i[1]})
    # key_list = list(a_dictionary.keys())
    # val_list = list(a_dictionary.values())
    # pos = val_list.index(max_val)
    return a_dictionary
