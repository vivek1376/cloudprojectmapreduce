#!/usr/bin/env python3

import sys
import re

infile = sys.stdin

# ignore header row
next(infile)

for line in infile:
    #print(line)

    line = line.strip()
    searchobj = re.search(r'^(([^,]*,){6})("\([0-9.]*,[-0-9. ]*\)")?,([^,]*,){17}(.*)', line)

    if not searchobj:
        continue

    vehicles = searchobj.group(5).split(',')
    for vehicle in vehicles:

        # namesearch = re.search(r'.*(\w.*\w).*', vehicle)

        # if not namesearch:
        #     continue

        # vehicle = namesearch.group(1)
        vehicle = vehicle.upper()

        if not vehicle:
            continue

        print(vehicle + "\t1")
            

        
