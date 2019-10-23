def boolean(x: bool, y: bool, op: str) -> bool:
    operations = {
        "conjunction": x and y,
        "disjunction": x or y,
        "implication": not x or y,  # not (x and not y)
        "exclusive": x ^ y,
        "equivalence": x == y
    }
    if op not in operations: raise TypeError("Boolean operation not supported")
    return operations[op]


if __name__ == '__main__':
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
    print('All good! Go and check the mission.')
