# https://py.checkio.org/mission/cakes-rows/publications/coells/python-3/first/share/b2b7b71fbccf21506e4d9a0714f242f0/
from math import pi
from cmath import phase

# just an idea ...
def checkio(data):
    translated = [[phase((x - x0) + 1j * (y - y0)) % pi for x, y in data if x != x0 or y != y0] for x0, y0 in data]
    print(translated)
    lined_up = sum(1 / (row.count(x) + 1) for row in translated for x in set(row) if row.count(x) > 1)
    return round(lined_up)
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
