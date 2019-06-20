#!/usr/bin/env python
move = input("Input step: ",)

position_x = 0
position_y = 0

count = len(move)

for i in range(count):
    if move[i] == "U":
        position_y += 1
    elif move[i] == "D":
        position_y -= 1
    elif move[i] == "L":
        position_x += 1
    elif move[i] == "R":
        position_x -= 1

if (position_x == 0) and (position_y == 0):
    print("True")
else:
    print("False")
