def neighbors(data, point):
    x, y = point
    neighbor_xy = [[x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]]
    return {(a, b): data[a][b] for a, b in neighbor_xy if 0 <= a < len(data) and 0 <= b < len(data[0])}


def can_pass(matrix, first, second):
    value = matrix[first[0]][first[1]]

    def move_to(neighbor, past_moves):
        if second in neighbor: return second
        for key in neighbor:
            if neighbor[key] == value and key not in past_moves: return key
        return None

    movements = [first]
    next_xy = move_to(neighbors(matrix, first), movements)
    print(next_xy)
    while next_xy != second:
        if next_xy is None: return False
        movements.append(next_xy)
        next_xy = move_to(neighbors(matrix, next_xy), movements)
    return True


if __name__ == '__main__':
    assert can_pass(((0, 5, 0, 5),
                     (0, 0, 0, 5),
                     (5, 5, 0, 5)),
                    (1, 0), (1, 1)) == True

    assert can_pass(((5, 6),
                     (6, 6),
                     (6, 5),
                     (6, 6),
                     (7, 6),
                     (6, 6),
                     (6, 7),
                     (6, 6),
                     (8, 6),
                     (6, 6)),
                    (9, 1), (0, 1)) == True
    assert can_pass(((0, 0),
                     (0, 0)),
                    (0, 0), (1, 1))

    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
