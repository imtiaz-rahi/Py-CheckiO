from typing import List
from math import acos, degrees


def angle(a: int, b: int, c: int):
    cos_c = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    return round(degrees(acos(cos_c))) if -1 < cos_c < 1 else 0


def checkio(a: int, b: int, c: int) -> List[int]:
    a1 = angle(b, c, a)
    if a1 == 0:
        return [0, 0, 0]
    a2 = angle(c, a, b)
    return sorted([a1, a2, (180 - a1 - a2)])


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(5, 4, 3) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")
