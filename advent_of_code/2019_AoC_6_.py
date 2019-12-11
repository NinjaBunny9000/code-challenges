# Puzzle: https://adventofcode.com/2019/day/6

from datetime import datetime
import pprint

startTime = datetime.now()
pp = pprint.PrettyPrinter(indent=4)

"""
Puzzle Notes

- AAA)BBB means BBB is in orbit around AAA
- maps need to be verified via "orbit count checksums"
    - checksums validate the total number of direct and indirect orbits
- if A orbits B and B orbits C, A indirectly orbits C (if A=>B && B=>C, A=>C)

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L

['COMB','BC','CD','DE','EF','BG', 'GH','DI','EJ','JK','KL']

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I

TOTAL = 42

H = 3+2+1 = 6
I = 4+3+2 = 7
L = 7+6+5+4 = 22
F = 5 = 40

EST (w/ COM) = 59
EST (w/o COM) = 40

- Check if the L obj in the list
    - If it is, replace it with R
    - if it isn't, append it to the list

Tails = ['F','H','I','L']

[COM, B, C, D, E, F] len=6 => 5+4+3+2+1=15
[B, G, H] len=4 => 3+2+1=6
[D, I] len=5 => 4+3+2+1=10
[E, J, K, L] len=8 => 7+6+5+4+3+2+1=28

D>C>B>COM = 3
C>B>COM = 2
B>COM = 1

total = 6
"""

class Orbits:

    def __init__(self):
        self.orbit_map = {}
        self.head = None
        # self.tail = None
        self.tails = []
        self.orbit_tracker = []
        self.branches = []

    def add(self, data, prev):
        prev = None if data == 'COM' else prev
        self.orbit_map[data] = prev
        self.head = prev if self.head is None else self.head
        # self.tail = data
        # self.tails[self.tails.index(prev)] = data if prev in self.tails else self.tails.append(data) # keep track of branch tails
        if prev in self.tails:
            self.tails[self.tails.index(prev)] = data
        else:
            self.tails.append(data)

    def traverse(self, tail):  # pass in a starting tail
        counter = 0  # DEBUG test counter for orbits
        prev_orbit = tail
        print(f"\nTRAVERSING BRANCH {tail}")
        branch = []
        while prev_orbit is not None:
            orbit = str(self.orbit_map[prev_orbit]) + prev_orbit
            # print(f"{orbit=}")
            branch.insert(0,orbit)
            prev_orbit = self.orbit_map[prev_orbit]
            if orbit in self.orbit_tracker:
                print(f"{orbit} already in orbit_tracker")
                counter += self.orbit_tracker
                break
            else:
                self.orbit_tracker.insert(0,orbit)
                counter += 1
        branches.append(branch)
        print(f"{branch=}")
        print(f"{self.orbit_tracker=}")
        return counter

    def get_length(self, tail):
        print(f"{tail=}")
        return self.traverse(tail)

    def get_tails(self):
        return self.tails

def orbit_validator(map_data):

    i = 0

    # parse everythign out into a list

    orbits = Orbits()

    orbits.add(map_data[0][:-1], None)

    # iterate thru the list and add the orbit coords as nodes in a linked list
    for _ in map_data:

        # parse the data out into something useable

        # print(f"{map_data[i]=}")  # DEBUG
        obj = map_data[i][-1]  # object in orbit
        orbiting = map_data[i][:-1]  # object it's orbiting
        # print(f"orbit detected: {obj=} {orbiting=}")  # DEBUG
        # create the node and add it to a list
        orbits.add(obj, orbiting)

        # print(f"STORED: {i=} {obj=} {orbiting=}")
        i += 1

    print('map:')
    pprint.pprint(orbits.orbit_map)
    print()

    total_orbits = 0

    print(f"{orbits.orbit_tracker=}")

    for tail in orbits.get_tails():
        # get length of the current tree and sum it's orbits
        length = orbits.get_length(tail)
        print(f"branch {tail} traversed! {length=}")
        sum_of_orbits = 0
        while length > 0:
            sum_of_orbits += length - 1
            length -= 1
        total_orbits += sum_of_orbits
        print(f"{sum_of_orbits=}")
        

    print(f"{total_orbits=}")
    print(f"{orbits.orbit_tracker=}")


    # final_coord = orbits[-1]
    # print(f"{final_coord=}")

    return "Done."

# print(orbit_validator(['COMB','BC','CD'])) # test (no branches)
print(orbit_validator(['COMB','BC','CD','DE','EF','BG', 'GH','DI','EJ','JK','KL'])) # test (with branches)
# print(orbit_validator()) # the full test

print(f"Run time: {datetime.now() - startTime}")
