def checkio(first, second):
    length = len(bin(second)[2:])

    score = 0
    for bitdigit in bin(first)[2:]:
        num = int(bitdigit*length, 2)
        score += (num & second) + (num | second) + (num ^ second)

    return score
