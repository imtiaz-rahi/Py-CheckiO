OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation) -> bool:
    if operation not in OPERATION_NAMES: raise TypeError("Boolean operation not supported")
    equivalence = lambda a, b: a == b
    conjunction = lambda a, b: a and b
    disjunction = lambda a, b: a or b
    implication = lambda a, b: False if a == 1 and b == 0 else True # not (a and not b)
    exclusive = lambda a, b: a+b % 2 == 1
    return locals()[operation](x, y)


if __name__ == '__main__':
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
    print('All good! Go and check the mission.')
