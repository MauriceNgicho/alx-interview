#!/usr/bin/python3


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        # Generate next row by adding adjacent elements in the previous row
        row = [1]  # First element is always 1
        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
