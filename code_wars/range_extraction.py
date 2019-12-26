# Kata: https://www.codewars.com/kata/range-extraction/train/python

import time
import pprint

star_time = time.time_ns()
pp = pprint.PrettyPrinter()

def format_ranges(ranges):
    listyboi = []
    for r in ranges:
        # handle single entries
        if len(r) <= 2:
            for n in r:
                listyboi.append(str(n))
        # handle ranges
        else:
            listyboi.append(f"{r[0]}-{r[-1]}")
    return ','.join(listyboi)

def solution(nums):
    nums.sort()
    ranges = []
    sequence = False

    for i,n in enumerate(nums):
        if not sequence:
            sequence = [n]
        # if the number is in sequence, add it to the current sequence
        elif n-1 == sequence[-1]:
            sequence.append(n)
        # if the number breaks a sequence
        else:
            ranges.append(sequence)
            sequence = [n]
        # add the last n in nums
        if i+1 == len(nums):
            ranges.append(sequence)

    return format_ranges(ranges)

print(solution([-3,-2,-1,2,10,15,16,18,19,20])) # '-3--1,2,10,15,16,18-20'
# print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])) # '-6,-3-1,3-5,7-11,14,15,17-20'

print(f"Run time: {time.time_ns() - star_time} ns")
