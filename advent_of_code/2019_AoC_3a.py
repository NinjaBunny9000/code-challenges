# Puzzle: https://adventofcode.com/2019/day/3

from datetime import datetime
import pprint

startTime = datetime.now()
pp = pprint.PrettyPrinter()

sample1 = [['R8','U5','L5','D3'],['U7','R6','D4','L4']]
sample2 = [['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']]
sample3 = [['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]
"""
Puzzle Notes

- 
"""

def crossed_wires():
    pass

print(crossed_wires(sample1)) # 6
print(crossed_wires(sample2)) # 159
print(crossed_wires(sample3)) # 135
print(crossed_wires()) # the full test

print(f"Run time: {datetime.now() - startTime}")