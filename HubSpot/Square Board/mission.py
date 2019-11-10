from typing import Tuple
Coordinate = Tuple[int, int]


def square_board(side: int, token: int, steps: int) -> Coordinate:
    return (0, 0)

if __name__ == '__main__':
    print("Example:")
    print(square_board(4, 1, 4))
    assert square_board(4, 1, 4) == (1, 0)
    assert square_board(6, 2, -3) == (4, 5)

    print("Coding complete? Click 'Check' to earn cool rewards!")

