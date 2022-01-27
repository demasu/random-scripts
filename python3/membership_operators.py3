#!/usr/bin/env python3

import pprint

all_lists = [
    ["ONE", "TWO", "THREE"],
    ["one", "two", "three"],
    [1, 2, 3],
    [123, 456, 789],
    ["1", "2", "3"],
    ["123", "456", "789"]
]

x = "one"
y = 2

print("Searching for [{}], and [{}] in the following lists:\n{}\n\n".format(x, y, pprint.pformat(all_lists, indent=4)) )

for i in all_lists:
    if x in i:
        print( "[{}] is found in the list {}".format(x, i) )

    if y in i:
        print( "[{}] is found in the list {}".format(y, i) )
