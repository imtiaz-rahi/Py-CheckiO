def inscribe(contour):
    # your code here

    return 0.0


if __name__ == '__main__':
    print("Example:")
    print(inscribe([(1, 1), (1, 2), (0, 2), (3, 5), (3, 4), (4, 4)]))

    def close_enough(contour, answer):
        result = inscribe(contour)
        assert abs(result - answer) <= 1e-3, \
            f'inscribe({contour}) == {answer}, and not {result}'

    # These "asserts" are used for self-checking and not for an auto-testing
    close_enough([(1, 1), (1, 2), (0, 2), (3, 5), (3, 4), (4, 4)], 6.0)
    close_enough([(6, 5), (10, 7), (2, 8)], 20.0)
    close_enough([(2, 3), (3, 8), (8, 7), (9, 2), (3, 2), (4, 4), (6, 6), (7, 3), (5, 3)], 41.538)
    close_enough([(0, 0), (0, 10), (0, 20), (100, 20), (100, 30), (120, 30), (120, 20), (120, 10), (20, 10), (20, 0)], 2679.208)
    close_enough([(10, 250), (60, 300), (300, 60), (250, 10)], 24000.0)
    close_enough([(10, 250), (60, 300), (110, 250), (160, 300), (210, 250), (160, 200), (300, 60), (250, 10)], 48000.0)
    print("Coding complete? Click 'Check' to earn cool rewards!")