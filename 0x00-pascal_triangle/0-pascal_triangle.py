#!/usr/bin/python3
"This is Pascal's Triangle"


def pascal_triangle(n):
    "Creates a list of lists of integers
    representing the Pascal's triangle of
    a given integer"
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for x in range(n):
        line = []
        for y in range(x + 1):
            if y == 0 or y == x:
                line.append(1)
            elif x > 0 and y > 0:
                line.append(triangle[x - 1][y - 1] + triangle[x - 1][y])
        triangle.append(line)
    return triangle
