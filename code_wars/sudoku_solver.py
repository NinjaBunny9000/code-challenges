# Kata: https://www.codewars.com/kata/529bf0e9bdf7657179000008

import time
import pprint
from collections import Counter

star_time = time.time_ns()
pp = pprint.PrettyPrinter()

"""
Notes

- returns True if valid solution, False otherwise
- 1 or more 0's is invalid (False)
- board is always 9x9 cells and contains integers from 0 to 9
"""

solution_1 = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
] # => true

solution_2 = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
] # => false

solution_3 = [
  [5, 3, 4, 6, 6, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
] # => false

solution_4 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]

# ideas:
# - sort then compare (d: doesn't account for 0's)
    # array.sort()
    # test_array = [1,2,3,4,5,6,7,8,9]
# - checking for duplicates 0,9 (using a set)

def confirm_digits(array):
    # checking for duplicates 0,9 (using counter)
    counter = Counter(array)
    dupes = [key for (key, value) in counter.items() if value > 1 and key]
    if dupes:
        print(f"dupes = {dupes}")
        return False
    return True


def validate_9x9(solution):
    zeroes = 0
    pp.pprint(solution)
    for line in solution:
        if confirm_digits(line) is False:
            print("failed confirm_digits")
            return False
        for num in line:
            if num == 0:
                zeroes += 1
                if zeroes > 1:
                    return False
                    print("failed zeros")

    return True


def validSolution(solution):

    # create a rotated array
    solution_rotated = [[],[],[],[],[],[],[],[],[]]
    for line in solution:
        for i,num in enumerate(line):
            solution_rotated[i].append(num)
    # pp.pprint(solution_rotated)        
    
    solution_3x3 = [[],[],[],[],[],[],[],[],[]]
    # split up into 9x 3x3 arrays 
    for i,line in enumerate(solution):
        
        pass



    print(f"{validate_9x9(solution)}")
    print(f"{validate_9x9(solution_rotated)}")

    # validated line by line
    if validate_9x9(solution) and validate_9x9(solution_rotated):
        return True
    else:
        return False


print(validSolution(solution_1)) # true
# print(validSolution(solution_2)) # false (multiple zero's)
# print(validSolution(solution_3)) # false (dupes)

print(f"Run time: {time.time_ns() - star_time} ns")







