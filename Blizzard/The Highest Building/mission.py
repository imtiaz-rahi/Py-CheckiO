def highest_building(buildings):
    #replace this for solution
    return 0

if __name__ == '__main__':
    print("Example:")
    print(highest_building([
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert highest_building([
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]) == [3, 4], "Common"
    assert highest_building([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]) == [4, 1], "Cabin in the wood"
    assert highest_building([
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1]
    ]) == [1, 5], "Triangle"
    assert highest_building([
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]) == [4, 6], "Pyramid"
    print("Coding complete? Click 'Check' to earn cool rewards!")