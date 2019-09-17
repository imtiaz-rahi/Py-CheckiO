from itertools import combinations
from collections import Counter

# def slope(x, y):
#     if x[0] - y[0] == 0: return None
#     return (x[1] - y[1]) / (x[0] - y[0])

def slope(a: tuple):
    if a[0][0] - a[1][0] == 0: return None
    return (a[0][1] - a[1][1]) / (a[0][0] - a[1][0])

def collinear(a: tuple) -> bool:
    return (a[0][1] - a[1][1]) * (a[0][0] - a[2][0]) == (a[0][1] - a[2][1]) * (a[0][0] - a[1][0])

def checkio(cakes):
    dict1 = {'key': 'value'}
    for it in combinations(cakes, 2):
        print(slope(it))
        x, y = it
        print(f'x={x}, y={y}')
    # for x, y in combinations(cakes, 2):
        # print(f'x={x}, y={y}')
        # print(slope(x, y))
        # dict1[(x, y)] = slope(x, y)
        # dict1[str(slope(x, y))] = {x, y}
    print(dict1)
    # b = [str(slope(it)) for it in combinations(cakes, 2)]
    # b = Counter(filter(lambda x: x != 'None', b))
    # print(b)
    # b = [k for k, v in b.items() if v >= 3]
    # print(b)
    return 1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
