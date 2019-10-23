from math import pi, sqrt, asin, atanh


def prolate(h, w):
    vol = 4/3 * pi * (w ** 2) * h
    e = sqrt(1 - w**2/h**2)
    area = 2 * pi * (w ** 2) * (1 + h/(w*e) * asin(e))
    return [round(vol, 2), round(area, 2)]


def oblate(h, w):
    vol = 4/3 * pi * (w ** 2) * h
    e2 = 1 - h**2/w**2
    e = sqrt(e2)
    area = 2 * pi * (w ** 2) * (1 + (1-e2)/e * atanh(e))
    return [round(vol, 2), round(area, 2)]


def sphere(radius: int):
    return [round(4 / 3 * pi * (radius ** 3), 2), round(4 * pi * (radius ** 2), 2)]


def checkio(h, w):
    """
    :param h: Height
    :param w: Width
    :return:
    """
    return sphere(h / 2) if h == w else prolate(h/2, w/2) if h > w else oblate(h/2, w/2)


if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
