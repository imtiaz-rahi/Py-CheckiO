# https://stackoverflow.com/questions/47604046/python-diagonal-match-in-a-2-dimensional-array
from typing import List


def max_is(best: str, arr: list) -> str:
    val = str(arr.count("O")) + "O"
    cxx = str(arr.count("X")) + "X"
    if cxx > val: val = cxx
    # item = max(["X", "O"], key=arr.count)
    # valu = str(arr.count(item)) + item
    return val if val > best else best


def checkio(game_result: List[str]) -> str:
    tic = "1"
    for i in range(0,3):
        # Get all items in column[i]
        tic = max_is(tic, [it[i] for it in game_result])
        # Get all items in row[i]
        # N.B. for some reason game_result[i:][:1] is returning 'XXX' not ['X', 'X', 'X]
        # So this weird hack to make it proper list (array)
        tic = max_is(tic, list(".".join(game_result[i:][:1])))

    # Get diagonal items (NE - SW)
    tic = max_is(tic, [game_result[0][0], game_result[1][1], game_result[2][2]])
    # Get diagonal items (NW - SE)
    tic = max_is(tic, [game_result[0][2], game_result[1][1], game_result[2][0]])

    return tic[1] if tic[0] == "3" else "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    assert checkio([
        "OOO",
        "XX.",
        ".XX"]) == "O", "Os wins"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
