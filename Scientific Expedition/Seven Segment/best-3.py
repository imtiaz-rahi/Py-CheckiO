# https://py.checkio.org/mission/seven-segment/publications/kurosawa4434/python-3/intersection-issubset-union/
from string import ascii_uppercase, ascii_lowercase

'''
    /-A-/  /-a-/
   F   B  f   b
  /-G-/  /-g-/
 E   C  e   c
/-D-/  /-d-/
'''

NUMS = [{'a', 'b', 'c', 'd', 'e', 'f'},
        {'b', 'c'},
        {'a', 'b', 'g', 'e', 'd'},
        {'a', 'b', 'g', 'c', 'd'},
        {'b', 'c', 'g', 'f'},
        {'a', 'c', 'd', 'f', 'g'},
        {'a', 'c', 'd', 'e', 'f', 'g'},
        {'a', 'b', 'c'},
        {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        {'a', 'b', 'c', 'd', 'f', 'g'}]


def seven_segment(lit_seg, broken_seg):

    lit_left = set(map(str.lower, lit_seg & set(ascii_uppercase)))
    lit_right = lit_seg & set(ascii_lowercase)
    broken_left = set(map(str.lower, broken_seg & set(ascii_uppercase)))
    broken_right = set(ascii_lowercase) & broken_seg

    d1 = list(filter(lambda n: lit_left <= n <= lit_left | broken_left, NUMS))
    d2 = list(filter(lambda n: lit_right <= n <= lit_right | broken_right, NUMS))

    return len(d1) * len(d2)


if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
