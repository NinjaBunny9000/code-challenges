# Kata: 

from datetime import datetime
import pprint

startTime = datetime.now()
pp = pprint.PrettyPrinter()


"""
Notes
- given an nxn array, rearrange elements from outtermost to middle
- traveling clockwise
"""

# new_list = [expression for member in iterable if variable condition]
# new_list = [expression (if conditional) for member in iterable]

test_array = [[1,2,3],[4,5,6],[7,8,9]]

"""
[1,2,3]
[4,5,6]
[7,8,9]

traverse
take the value of x,y
right
new_array.append(array[y+0][x+0])
new_array.append(array[y+0][x+1])
new_array.append(array[y+0][x+2])
down
new_array.append(array[y+1][x+2])
new_array.append(array[y+2][x+2])
left
new_array.append(array[y+2][x+1])
new_array.append(array[y+2][x+0])
up
new_array.append(array[y+1][x+0])
right
new_array.append(array[y+1][x+1])

row/col
right
(0,0)
(0,1)
(0,2)

down
(1,2)
(2,2)

left
(2,1)
(2,0)

up
(1,0)
(1,1)

"""
# TODO do this again but with removing the items from the original array
def snail_sort(array):

    new_array = []  # placeholder array

    # get the length and height of the array
    n = len(array[0])

    # set up "cursor" positions
    x = 0
    y = 0
    col = 0
    row = 0
    loop = 1


    while loop < n:

        print(f"starting loop {loop} // {row=} {col=}")

        # right
        for _ in range(n):
            new_array.append(array[row][col])
            col += 1

        # down
        row = loop
        col = n-loop
        for _ in range(n-loop):
            new_array.append(array[row][col])
            row += 1

        # left
        row = col
        col = n-row
        print(f"{row=}")
        print(f"row={n-col}")
        for _ in range(n-loop**loop):
            new_array.append(array[row][col])
            col -= 1

        # up
        row = loop
        col = loop-1
        for _ in range(loop):
            new_array.append(array[row][col])

        # reset for next loop and right move
        row = loop
        col = loop-row
        loop += 1




    return new_array


print(snail_sort(test_array)) # [1,2,3,6,9,8,7,4,5]
# print(snail_sort()) # the full test

print(f"Run time: {datetime.now() - startTime}")