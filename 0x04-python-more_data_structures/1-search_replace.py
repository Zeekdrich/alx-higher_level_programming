#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = []
    for x in my_list:
        if x == search:
            newList.append(replace)
        else:
            newList.append(x)
    return newList
