# https://py.checkio.org/mission/seven-segment/publications/mihail.ponomaryov/python-3/first/
DIGITS = [
    {'a', 'b', 'c', 'd', 'e', 'f'},
    {'b', 'c'},
    {'a', 'b', 'g', 'e', 'd'},
    {'a', 'b', 'g', 'c', 'd'},
    {'b', 'c', 'g', 'f'},
    {'a', 'c', 'd', 'f', 'g'},
    {'a', 'c', 'd', 'e', 'f', 'g'},
    {'a', 'b', 'c'},
    {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    {'a', 'b', 'c', 'd', 'f', 'g'}
]

def seven_segment(lit_seg, broken_seg):
    first_lit = {x.lower() for x in lit_seg if x.isupper()}
    first_broken = {x.lower() for x in broken_seg if x.isupper()}

    second_lit = {x for x in lit_seg if x.islower()}
    second_broken = {x for x in broken_seg if x.islower()}

    first_possible = len([d for d in DIGITS if d - first_broken == first_lit])
    second_possible = len([d for d in DIGITS if d - second_broken == second_lit])

    return first_possible * second_possible


if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
