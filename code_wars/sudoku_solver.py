# Kata: https://www.codewars.com/kata/529bf0e9bdf7657179000008

import time
import pprint
from collections import Counter

start_time = time.time_ns()
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

solution_5 = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 0, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 0, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
] # => true


def confirm_digits(line):
    """checks line by line for duplicates"""
    counter = Counter(line)
    dupes = [key for (key, value) in counter.items() if value > 1 and key]
    return not dupes


def validate_9x9(array):
    """validates solutions line by line on 9x9 array"""
    zeroes = 0  # fail if >1 zero in 9x9 array
    for line in array:
        if confirm_digits(line) is False:
            return False
        for num in line:
            if num == 0:
                zeroes += 1
                if zeroes > 1:
                    return False
    return True


def validSolution(solution):
    """validate a 9x9 sudoku solution"""
    
    # split up into 9x 3x3 arrays and validate them
    solution_3x3 = [[],[],[],[],[],[],[],[],[]]
    for i in range(2,9,3):
        # every 3 lines
        for j in range(2,9,3):
            # every 3 rows
            nine_by_nine = []
            nine_by_nine.append(solution[i-2][j-2])
            nine_by_nine.append(solution[i-2][j-1])
            nine_by_nine.append(solution[i-2][j])
            nine_by_nine.append(solution[i-1][j-2])
            nine_by_nine.append(solution[i-1][j-1])
            nine_by_nine.append(solution[i-1][j])
            nine_by_nine.append(solution[i][j-2])
            nine_by_nine.append(solution[i][j-1])
            nine_by_nine.append(solution[i][j])

            if confirm_digits(nine_by_nine) is False:
                return False

    # rotate the array/solution
    solution_rotated = [[],[],[],[],[],[],[],[],[]]
    for line in solution:
        for i,num in enumerate(line):
            solution_rotated[i].append(num)

    # validate 9x9 solution and a rotated version
    if validate_9x9(solution) and validate_9x9(solution_rotated):
        return True
    else:
        return False


# print(validSolution(solution_1)) # true
# print(validSolution(solution_2)) # false (dupes)
# print(validSolution(solution_3)) # false (dupes)
# print(validSolution(solution_4)) # false (dupes)
print(validSolution(solution_5)) # false (mult zeros)

print(f"Run time: {time.time_ns() - start_time} ns")







