def probability(w: int, b: int, step: int):
    wp = w / (w + b)
    if step == 1: return wp
    return wp * probability(w-1, b+1, step-1) + ((1-wp) * probability(w+1, b-1, step-1))


def checkio(marbles: str, step: int) -> float:
    return round(probability(marbles.count('w'), marbles.count('b'), step), 2)


if __name__ == '__main__':
    print("Example:")
    print(checkio('bbw', 3))

    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
