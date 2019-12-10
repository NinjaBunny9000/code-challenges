# Puzzle: https://adventofcode.com/2019/day/6

from datetime import datetime

startTime = datetime.now()

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

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I

TOTAL = 42

"""

class OrbitMap:
    """A linked-list that stores and operates on orbit map data."""

    def __init__(self, obj, prev=None):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f"{self.obj=} {self.prev=}"

    def add(self, obj, prev):
        """adds an object node to the linked-list"""
        if not isinstance(obj, OrbitMap):
            obj = ListNode(obj)
        self.head = obj if self.head is None else self.tail.prev = obj
        self.tail = obj

    def has_value(self, val):
        return self.data == val

    def list_length(self):
        length = 0
        current_node = self.tail
        while current_node is not None:
            length += 1  # count the node
            current_node = current_node.prev  # count the next one
        return length

    def unordered_search(self):
        pass

    def traverse(self):
        current_node = self.tail
        orbits = 0
        while current_node is not None:
            print(f"{orbit=}")
            current_node = current_node.prev
            orbits += 1
            print(f"orbits so far = {orbits}")
        print(f"{orbits=}")


def orbit_validator(map_data):

    orbits = list()  # create a list of orbit
    i = 0

    # parse everythign out into a list

    for _ in map_data:

        obj = map_data[i][-1]  # object in orbit
        orbiting = map_data[i][:-1]  # object it's orbiting
        print(f"STORED: {i=} {obj=} {orbiting=}")

        new_node = OrbitNode(obj, orbiting)
        OrbitNode.add(new_node)
        # handle the first input (COM=>?)
        # if map_data[i][:3] == 'COM':

        # # handle other entries
        # else:
        #     OrbitNode(obj, orbiting)

        i += 1

    final_coord = orbits[-1]
    print(f"{final_coord=}")

    final_coord.traverse()



print(orbit_validator(['COMB','BC','CD'])) # test
# print(orbit_validator()) # the full test

print(f"Run time: {datetime.now() - startTime}")