from operator import or_, and_, xor


def checkio(first, second, result=0):
    first = [int(c) for c in bin(first)[2:]]
    second = [int(c) for c in bin(second)[2:]]
    for ope in and_, or_, xor:
        result += sum(int(''.join(str(ope(x, y)) for y in second), 2) for x in first)
    return result


if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
