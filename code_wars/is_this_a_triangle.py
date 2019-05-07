# https://www.codewars.com/kata/56606694ec01347ce800001b/train/python

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(is_triangle(1, 2, 2))
print(is_triangle(7, 2, 2))
print(is_triangle(4, 2, 3))
print(is_triangle(5, 1, 5))
print(is_triangle(2, 2, 2))
print(is_triangle(-1, 2, 3))
print(is_triangle(1, -2, 3))
print(is_triangle(1, 2, -3))
print(is_triangle(0, 2, 3))