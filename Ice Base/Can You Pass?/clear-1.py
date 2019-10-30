# https://py.checkio.org/mission/can-pass/publications/gyahun_dash/python-3/itertools/
from itertools import chain, product, starmap


def can_pass(matrix, first, second):
    digit = matrix[first[0]][first[1]]
    cells = product(range(len(matrix)), range(len(matrix[0])))
    living = {(y, x) for y, x in cells if matrix[y][x] == digit}

    neighbors = lambda y, x: ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1))
    tips = {first}
    while tips:
        tips = set(chain.from_iterable(starmap(neighbors, tips))) & living
        living -= tips
        if second in tips: return True

    return False


if __name__ == '__main__':
    assert can_pass(((0, 5, 0, 5),
                     (0, 0, 0, 5),
                     (5, 5, 0, 5)),
                    (1, 0), (1, 1)) == True

    assert can_pass(((5, 6),
                     (6, 6),
                     (6, 5),
                     (6, 6),
                     (7, 6),
                     (6, 6),
                     (6, 7),
                     (6, 6),
                     (8, 6),
                     (6, 6)),
                    (9, 1), (0, 1)) == True
    assert can_pass(((0, 0),
                     (0, 0)),
                    (0, 0), (1, 1))

    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
