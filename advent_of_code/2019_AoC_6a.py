# Puzzle: https://adventofcode.com/2019/day/6

import time
import pprint
from collections import defaultdict

star_time = time.time_ns()
pp = pprint.PrettyPrinter()

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

        2   3       5   6   7
        G - H       J - K - L
       /      3    /
COM - B - C - D - E - F
      1   2    \  4   5
                I
                4

H = 1+2+3 = 6
I = 2+3+4 = 9
L = 4+5+6+7 = 22
F = 5
TOTAL = 42

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

# TODO make this count things via next
# TODO use count_orbits

class OrbitMapper:

    def __init__(self):
        self.orbit_map = {}  # linked list/map of all the orbits
        self.head = None  # start of the linked list
        self.tails = []  # list of tails
        self.orbit_counter = 0
        self.branch_head = None

    # TODO make it work with lists for values
    def add(self, body, next_body):
        self.head = body if self.head is None else self.head  # set the head
        # add node to the linked list
        try:
            # TODO make this cleaner w/o the except
            node = list(self.orbit_map[body])
        except KeyError:
            node = []
        node.append(next_body)
        self.orbit_map[body] = node
        self.orbit_map[next_body] = []  # keep track of branch tails

    #  TODO if you are doing recusion you need to pass the currentTotal by ref and current depth
    def count_orbits_but_better(self, body):
        # TODO when it reaches a tail, reset the counter to the one before the branch + 1
        if self.orbit_map[body] == []:
            print("tail reached")
            return

        # TODO figure out if it's a head
        for branch in self.orbit_map[body]:
            print(f"counting {body=}. {branch=} next={self.orbit_map[branch]}")
            self.orbit_counter += 1
            self.count_orbits_but_better(branch)


orbit_mapper = OrbitMapper()

def orbit_validator(map_data):

    # separate the data into data and next loc and add the note to the linked list
    for i,node in enumerate(map_data):
        body = map_data[i][:-1]
        next_body = map_data[i][-1]
        orbit_mapper.add(body, next_body)

    pp.pprint(orbit_mapper.orbit_map)
    # orbit_mapper.count_orbits(orbit_mapper.head)
    orbit_mapper.count_orbits_but_better(orbit_mapper.head)
    print(f"Total orbits: {orbit_mapper.orbit_counter}")
    return "Done."



# print(orbit_validator(['COMB','BC','CD'])) # test (no branches)
print(orbit_validator(['COMB','BC','CD','DE','EF','BG', 'GH','DI','EJ','JK','KL'])) # test (with branches)
# print(orbit_validator()) # the full test


print(f"Run time: {time.time_ns() - star_time} ns")
