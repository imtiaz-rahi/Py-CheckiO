# https://py.checkio.org/mission/find-enemy/publications/Pouf/python-3/so-easy/share/665d68f2b2929242e2592ecb67dad9b2/
from math import sin, cos, acos, hypot, degrees, pi
from operator import mul


def find_enemy(you, dir, enemy):
    x, y = zip(you, enemy)
    x = [ord(L)-65 for L in x]
    y = [int(n) + x[i] % 2 / 2 for i, n in enumerate(y)]
    u = [(x[1] - x[0]) * sin(pi/3), y[1] - y[0]]
    a = {'N': pi, 'NE': pi*2/3, 'SE': pi/3, 'S': 0, 'SW': pi*5/3,
         'NW': pi*4/3}.get(dir)
    v = [sin(a), cos(a)]
    angle = degrees(acos(sum(map(mul, u, v)) / hypot(*u)))
    if angle < 59.9:
        result = ['F']
    elif angle < 120.1:
        left = u[0] * v[1] - u[1] * v[0] > 0
        result = [['R', 'L'][left]]
    else:
        result = ['B']
    dist = abs(u[0] / sin(pi/3))
    dist += max(0, abs(u[1]) - dist * .5)
    result.append(round(dist))
    return result

if __name__ == '__main__':
    assert find_enemy('B2', 'S', 'B4') == ['F', 2]
    assert find_enemy('G5', 'N', 'G4') == ['F', 1], "N-1"
    assert find_enemy('G5', 'N', 'I4') == ['R', 2], "NE-2"
    assert find_enemy('G5', 'N', 'J6') == ['R', 3], "SE-3"
    assert find_enemy('G5', 'N', 'G9') == ['B', 4], "S-4"
    assert find_enemy('G5', 'N', 'B7') == ['L', 5], "SW-5"
    assert find_enemy('G5', 'N', 'A2') == ['L', 6], "NW-6"
    assert find_enemy('G3', 'NE', 'C5') == ['B', 4], "[watch your six!]"
    assert find_enemy('H3', 'SW', 'E2') == ['R', 3], "right"
    assert find_enemy('A4', 'S', 'M4') == ['L', 12], "true left"
    print("You are good to go!")
