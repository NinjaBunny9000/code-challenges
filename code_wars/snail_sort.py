# Kata: https://www.codewars.com/kata/snail/train/python

from datetime import datetime
import pprint

startTime = datetime.now()
pp = pprint.PrettyPrinter()

"""
Notes
- given an nxn array, rearrange elements from outtermost to middle
- traveling clockwise

EXAMPLE 3x3: [1,2,3]
             [4,5,6]
             [7,8,9]

SHOULD EQUAL: [1,2,3,6,9,8,7,4,5]
"""

def snail(array):
    
    # confirm n by n array
    if isinstance(array[0], list) is False:
        print("Array is not n by n.")
        return 0

    # get array dimms
    n = len(array[0])
    print(f"Array is {n} by {n}:")
    pp.pprint(array)  # print out the array we take in
    sorted_array = []
    iterations = 0  # track how many times around we go (for funsies)

    
    while True:

        # take off the top row (left to right)
        print('\n1) L=>R')
        if len(array) == 0:
            break
        # print("L->R")
        for item in array[0]:
            sorted_array.append(item)
        array.pop(0)
        pp.pprint(array)
            
        # take off everything on the ends (top to bottom)
        if len(array) == 0:
            break
        print('\n2) U=>D')
        for row in array:
            sorted_array.append(row[-1])  # get last item on every row
            number = row[-1]
            array[array.index(row)].pop(-1)
        pp.pprint(array)

        # take off the borrom row (right to left)
        print('\n3) R=>L')
        if len(array) == 0:
            break
        for i in range(len(array[0])-1, -1, -1):
            sorted_array.append(array[-1][i])
        array.pop(-1)
        pp.pprint(array)

        # take the left (bottom to top)
        print('\n4) D=>U')
        if len(array) == 0:
            break
        for i in range(len(array)-1, -1, -1):
            # print(f"{array[i][0]}")
            sorted_array.append(array[i][0])
            array[i].pop(0)
        pp.pprint(array)

        iterations += 1

    print(f"\nSorted in {iterations} iterations.\n")

    return sorted_array

        
# INPUT/VALIDATION DATA
small_array = [[1,2,3],[4,5,6],[7,8,9]]
seven_by_seven = [[150, 291, 554, 225, 184, 493, 958], [441, 523, 686, 669, 710, 266, 53], [88, 397, 160, 252, 605, 448, 88], [364, 761, 169, 883, 968, 212, 748], [891, 253, 967, 877, 764, 80, 164], [901, 691, 752, 269, 33, 847, 160], [230, 195, 198, 674, 697, 93, 121]]

# TESTS
# print(snail(small_array)) # [1,2,3,6,9,8,7,4,5]
print(snail(seven_by_seven)) # [150, 291, 554, 225, 184, 493, 958, 53, 88, 748, 164, 160, 121, 93, 697, 674, 198, 195, 230, 901, 891, 364, 88, 441, 523, 686, 669, 710, 266, 448, 212, 80, 847, 33, 269, 752, 691, 253, 761, 397, 160, 252, 605, 968, 764, 877, 967, 169, 883]

print(f"Run time: {datetime.now() - startTime}")