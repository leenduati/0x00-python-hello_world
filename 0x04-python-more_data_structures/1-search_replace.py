#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = []

    for j in my_list:
        new_list.append(j)
    ind = 0

    for i in new_list:
        if i == search:
            ind = new_list.index(search)
            new_list[ind] = replace
        else:
            continue

    return new_list
