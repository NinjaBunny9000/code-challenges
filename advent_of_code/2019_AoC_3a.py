# Puzzle: https://adventofcode.com/2019/day/3

import time
import pprint

star_time = time.time_ns()
# startTime = datetime.now()
pp = pprint.PrettyPrinter()


grid = {
    # position, lines at point
    # (0,0) : []
}


movements = {
    'U' : [0,1],
    'D' : [0,-1],
    'L' : [-1,0],
    'R' : [1,0]
}


def crossed_wires(lines):
    # TODO pooping values from list as they're parsed to save memory
    # TODO finding each intersection at a time and comparing distance to prev intersection

    print("============================ CROSSED WIRES ============================\n")

    # moves = [0,0]  # DEBUG

    pp.pprint(lines)
    print()

    # for each line
    for i,line in enumerate(lines):
        cursor = [0,0] # reset the cursor location for a new line
        # prev_cursor = cursor

        # for each move in line
        for move in line:

            # moves[i] += 1  # DEBUG
            # parse the movement instructions
            direction = movements[move[0]]
            distance = int(move[1:])

            # make a coordinate for moves that need to be mave
            moving = tuple([axis*distance for axis in direction])
            # print(f"line={i} {move[0]=} {distance=} {moving=}")

            # establish the cursor location??
            prev_cursor = tuple(cursor) # [8,0]
            start = None
            # end = [0,0]

            # cursor = list()
            # print(f"{prev_cursor=}")

            # move the cursor for each step and mark the point in the grid
            x_step = 1 if moving[0] >= 0 else -1
            for x in range(0,moving[0] + x_step,x_step):

                y_step = 1 if moving[1] >= 0 else -1
                for y in range(0,moving[1] + y_step,y_step):

                    cursor[0] = x + prev_cursor[0]
                    cursor[1] = y + prev_cursor[1]
                    if tuple(cursor) not in grid:
                        grid[tuple(cursor)] = 1
                    elif grid[tuple(cursor)] == 1:
                        grid[tuple(cursor)] = 2
                    else:
                        print("fuckery afoot")


                    if start is None:
                        start = tuple(cursor)
                        print(f"{start=} line={i} {move[0]=} {distance=} {moving=}")

        print(f"End of line. {tuple(cursor)=}")


    shortest_dist = None
    origin = (0, 0)
    for k,v in grid.items():
        # count the manhatten distance of intersections (excluding origin)
        if v is 2 and k != origin:
            # print(f"{k[0]} {k[1]}")
            m_dist = abs(k[0]) + abs(k[1])
            int_loc = k
            print(f"{m_dist=}")
            if shortest_dist is None:
                shortest_dist = m_dist
                shortest_loc = int_loc
                print(f"\nFirst intersection located @ {int_loc}. Distance: {shortest_dist}.")
            elif m_dist < shortest_dist:
                shortest_dist = m_dist
                shortest_loc = int_loc
                print(f"Closer intersection detected @ {int_loc}. Distance: {shortest_dist}.")

    pp.pprint(grid)

    print(f"\nThe closest intersection is at {shortest_loc} and has a manhatten distance of {shortest_dist}.\n")

    return "================================ DONE ================================="


# sample0 = [['R8']]
# sample0 = [['R8','U5']]
# sample0 = [['R8','U5'],['U7','R6']]
# sample0 = [['R8','U5','L5','D3']]
# sample1 = [['R8','U5','L5','D3'],['U7','R6','D4','L4']]
sample2 = [['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']]
# sample3 = [['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]


# print(crossed_wires(sample0)) # TEST
# print(crossed_wires(sample1)) # 6
print(crossed_wires(sample2)) # 159
# print(crossed_wires(sample3)) # 135
# print(crossed_wires()) # the full test

print(f"Run time: {time.time_ns() - star_time} ns")