from operator import and_, or_, xor


def checkio(first, second):
    digits = lambda x: [int(d) for d in bin(x)[2:]]
    return sum(sum(int("".join(map(str, [opr(row, col)
                            for col in digits(second)])), 2)
                            for row in digits(first))
                            for opr in [and_, or_, xor])


if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
