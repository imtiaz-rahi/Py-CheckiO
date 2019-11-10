from typing import List

def checkio(puzzle: List[List[int]]) -> str:
    """
    Solve the puzzle
      U - up
      D - down
      L - left
      R - right
    """
    return "ULDR"


if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 2, 3],
                   [4, 6, 8],
                   [7, 5, 0]]))

    #This part is using only for self-checking and not necessary for auto-testing
    GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    MOVES = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def check_solution(func, puzzle):
        size = len(puzzle)
        route = func([row[:] for row in puzzle])
        goal = GOAL
        x = y = None
        for i, row in enumerate(puzzle):
            if 0 in row:
                x, y = i, row.index(0)
                break
        for ch in route:
            swap_x, swap_y = x + MOVES[ch][0], y + MOVES[ch][1]
            if 0 <= swap_x < size and 0 <= swap_y < size:
                puzzle[x][y], puzzle[swap_x][swap_y] = puzzle[swap_x][swap_y], 0
                x, y = swap_x, swap_y
        if puzzle == goal:
            return True
        else:
            print("Puzzle is not solved")
            return False

    assert check_solution(checkio, [[1, 2, 3],
                                    [4, 6, 8],
                                    [7, 5, 0]]), "1st example"
    assert check_solution(checkio, [[7, 3, 5],
                                    [4, 8, 6],
                                    [1, 2, 0]]), "2nd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")