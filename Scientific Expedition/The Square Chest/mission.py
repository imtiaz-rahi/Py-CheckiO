from typing import List

GRID = 4


def is_square(x: int, y: int, more: int, grid_lines: list) -> bool:
    if y - x == 4:
        return False
    x1 = x + GRID * (more + 1)  # bottom-left point
    y1 = y + more               # top-right point

    line_top = [[i + j for j in range(0, 2)] for i in range(x, y1)]
    line_bot = [[i + j for j in range(0, 2)] for i in range(x1, (x1 + 1) + more)]
    line_left = [[i + j for j in range(0, 5, GRID)] for i in range(x, x1, GRID)]
    line_right = [[i + j for j in range(0, 5, GRID)] for i in range(y1, y1 + GRID * (more + 1), GRID)]
    my_square = line_top + line_right + line_bot + line_left
    return all(elem in grid_lines for elem in my_square)


def checkio(lines_list: List[List[int]]) -> int:
    count = 0
    lines_list.sort()
    # redefine [x, y] to make sure x < y always
    for i, elem in enumerate(lines_list):
        (x, y) = elem
        if x > y:
            lines_list[i] = [y, x]

    for it in lines_list:
        (x, y) = it
        # check for next right points, if true square size will be bigger
        for more in range(1, GRID):
            count += is_square(x, y, more - 1, lines_list)
    return count


if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 2], [1, 5], [2, 6], [5, 6]]))
    print(checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                   [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                   [10, 14], [12, 16], [14, 15], [15, 16]]))

    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    assert checkio([[16, 15], [16, 12], [15, 11], [11, 12], [11, 10],
                        [10, 14], [9, 10], [14, 13], [13, 9], [15, 14]]) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
