#!/usr/bin/python3

"""
Builds the islands.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                for direction in directions:
                    x = i + direction[0]
                    y = j + direction[1]
                    if (x < 0 or x >= rows or y < 0
                            or y >= cols or grid[x][y] == 0):
                        perimeter += 1

    return perimeter
