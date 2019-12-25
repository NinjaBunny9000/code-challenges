# Kata: https://www.codewars.com/kata/sum-of-intervals/train/python

import time
import pprint

star_time = time.time_ns()
pp = pprint.PrettyPrinter()

test_1 = [
    (1,2),
    (6, 10),
    (11, 15)
]  # 9

test_2 = [
    (1,4),
    (7, 10),
    (3, 5)
]  # 7

test_3 = [
    (1,5),
    (10, 20),
    (1, 6),
    (16, 19),
    (5, 11)
]  # 19

test_4 = [
    (1,5),
    (1,5)
]  # 4


"""
Notes
- count the total ranges, excluding overlapping values
"""

def sum_of_intervals(ranges):

    ranges = [list(r) for r in ranges]  # convert tuples to a mutable list
    ranges.sort()
    sorted_ranges = False

    for i,r in enumerate(ranges):
        # start the list off with the first range
        if sorted_ranges is False:
            sorted_ranges = []
            sorted_ranges.append(r)
            continue
        
        overlap = False  # reset the overlap flag

        # check for any overlap and modify the range in sorted (if there is any)
        for j,s in enumerate(sorted_ranges):
            if r[0] < s[0] < r[1]:
                sorted_ranges[j][0] = ranges[i][0]
                overlap = True
            elif r[0] < s[1] < r[1]:
                sorted_ranges[j][1] = ranges[i][1]
                overlap = True
            elif r[0] >= s[0] and r[1] <= s[1]:
                overlap = True
            else:
                pass
        
        # if there was no overlap, add it to the end of the list
        if overlap is False:
            sorted_ranges.append(r)
        
    # do mathy stuffs to figure out the true range
    sum_of_ranges = 0
    for r in sorted_ranges:
        sum_of_ranges += r[1]-r[0]
    return sum_of_ranges


print(f"Solution: {sum_of_intervals(test_1)}") # 9
print(f"Solution: {sum_of_intervals(test_2)}") # 7
print(f"Solution: {sum_of_intervals(test_3)}") # 19
print(f"Solution: {sum_of_intervals(test_4)}") # 4

print(f"Run time: {time.time_ns() - star_time} ns")
