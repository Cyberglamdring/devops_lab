#!/usr/bin/env python
def dictmaker():
    "Work with dictionary"
    list1 = [i for i in input('Input keys separated by a space: ').split()]
    list2 = [i for i in input('Input values separated by a space: ').split()]
    dict(zip(list1, list2))
    return dict(zip(list1, list2))

print('Dictionary is:',dictmaker())