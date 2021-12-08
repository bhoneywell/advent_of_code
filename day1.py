#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:05:20 2021
Advent of Code Day 1
@author: bhoneywell
"""
import numpy as np


"""
Day 1 Part 1 

"""

with open('input.txt') as f:
    lines = f.read().splitlines()

prev_value = np.nan
counter = 0
for line in lines:
    curr_value = int(line)
    if curr_value > prev_value:
        counter += 1
    prev_value = curr_value
print(counter)
    
"""
Day 1 Part 2 

"""
    
values_sums = []
for i in range(2,len(lines)):
    val = int(lines[i-2]) + int(lines[i-1]) + int(lines[i])
    values_sums.append(val)

prev_value = np.nan
counter = 0
for v in values_sums:
    curr_value = v
    if curr_value > prev_value:
        counter += 1
    prev_value = curr_value
print(counter)
    