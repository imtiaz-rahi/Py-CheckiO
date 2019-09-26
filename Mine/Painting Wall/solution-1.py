__author__ = 'jingyuan'


def checkio(num, data):
    painted = []
    for k, i in enumerate(data):
        painted.append(i[:])
        painted.sort(key=lambda i: i[0])
        j = 0
        print(f'len={len(painted)}')
        for l in range(len(painted) - 1):
            if painted[j][1] >= painted[j + 1][0]:
                painted[j][1] = max(painted[j][1], painted[j + 1][1])
                painted.pop(j + 1)
            else:
                j += 1
        length = 0

        for l in painted:
            length += l[1] - l[0] + 1
        if length >= num:
            return k + 1
    return -1


if __name__ == '__main__':
    # assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
    # assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
    # assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
    # assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
    # assert checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
    # assert checkio(1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"
    assert checkio(15, [[1, 2], [20, 30], [25, 28], [5, 10], [4, 21], [1, 6]]) == 4
    # assert checkio(30, [[1, 2], [20, 30], [25, 28], [5, 10], [4, 21], [1, 6]]) == 6
    # assert checkio(6000,
    #               [[8598, 9442], [4221, 4432], [4864, 5415], [1315, 1960], [9577, 10482], [8147, 8346], [6063, 6836],
    #                [24, 606], [6170, 7131], [1397, 2020], [4690, 5651], [5267, 5464], [8422, 8886], [5547, 5738],
    #                [5722, 6511], [6605, 6905], [1321, 2242], [9335, 9993], [1626, 1887], [4699, 4926]]) == 15
