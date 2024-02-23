#!/usr/bin/env python3

with open('dataMaster/data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# some comment
