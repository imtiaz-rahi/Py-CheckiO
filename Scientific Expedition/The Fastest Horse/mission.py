from collections import Counter


def fastest_horse(*horses) -> int:
    if isinstance(horses[0][0], list): horses = horses[0]
    return Counter(it.index(min(it)) for it in horses).most_common()[0][0] + 1


if __name__ == '__main__':
    # print(fastest_horse([['1:13', '1:26', '1:11']]))
    # print(fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]))
    # print(fastest_horse(["4:44", "4:11", "4:18"], ["3:10", "3:01", "3:14"], ["2:20", "2:23", "2:15"]))

    assert fastest_horse(["4:44","4:11","4:18"],["3:10","3:01","3:14"],["2:20","2:23","2:15"]) == 2
    assert fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
