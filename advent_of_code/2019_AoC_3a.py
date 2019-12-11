# Puzzle: https://adventofcode.com/2019/day/3

from datetime import datetime
import pprint

startTime = datetime.now()
pp = pprint.PrettyPrinter()

sample1 = [['R8','U5','L5','D3'],['U7','R6','D4','L4']]
sample2 = [['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']]
sample3 = [['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]

grid = {
    # position, lines at point
    (0,0) : []
}

movements_dict = {
    'U' : {'x':0,'y':1},
    'D' : {'x':0,'y':-1},
    'L' : {'x':-1,'y':0},
    'R' : {'x':1,'y':0},
}

movements_tup = {
    'U' : (0,1),
    'D' : (0,-1),
    'L' : (-1,0),
    'R' : (1,0),
}

movements = {
    'U' : [0,1],
    'D' : [0,-1],
    'L' : [-1,0],
    'R' : [1,0],
}


def crossed_wires(lines):

    for line in lines:  # for each line
        cursor = ()
        for move in line:  # for each move in line
            # parse the movement instructions
            direction = movements_tup[move[0]]
            distance = move[-1:]
            # build list for cursor movements
            moving = [axis * int(distance) for axis in direction]
            print(f"{move[0]=} {direction=} {distance=} {moving=}")

            for i,axis in enumerate(moving):
                cursor = [0,0]
                for dist in range(axis + 1):
                    print(f"{i=} {dist=}")
                    # add point to the grid
                    grid[tuple(cursor)] = 
                    # move the cursor




    pp.pprint(grid)
            # mark grid for each movement

    return 'Done.'



print(crossed_wires(sample1)) # 6
# print(crossed_wires(sample2)) # 159
# print(crossed_wires(sample3)) # 135
# print(crossed_wires()) # the full test

print(f"Run time: {datetime.now() - startTime}")