def checkio(first, second):
    decimal = lambda x: int("".join(map(str, x)), 2)
    list_a, list_o, list_x = [], [], []
    for row in [int(d) for d in bin(first)[2:]]:
        row_a, row_o, row_x = [], [], []
        # Calculate and, or and xor of each number combination and put them in separate arrays
        for col in [int(d) for d in bin(second)[2:]]:
            row_a.append(row & col)
            row_o.append(row | col)
            row_x.append(row ^ col)
        # Binary numbers created from each array items are converted to decimal
        list_a.append(decimal(row_a))
        list_o.append(decimal(row_o))
        list_x.append(decimal(row_x))
    return sum(list_a) + sum(list_o) + sum(list_x)


if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
