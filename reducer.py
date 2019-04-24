#!/usr/bin/env python3


import sys

current_vehicle = None
current_count = 0
word = None

infile = sys.stdin

for line in infile:
    line = line.strip()

    vehicle, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue
    
    if current_vehicle == vehicle:
        current_count += count
    else:
        if current_vehicle:
            print(current_vehicle + "\t" + str(current_count))

        current_count = count
        current_vehicle = vehicle

if current_vehicle == vehicle:
    print(current_vehicle + "\t" + str(current_count))
