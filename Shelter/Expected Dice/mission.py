def expected(dice_number, sides, target, board):
    return 0.0

if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(expected(1, 4, 3, [0, 0, 0, 0]), 4.0))
    assert(almost_equal(expected(1, 4, 1, [0, 0, 0, 0]), 4.0))
    assert(almost_equal(expected(1, 4, 3, [0, 2, 1, 0]), 1.3))
    assert(almost_equal(expected(1, 4, 3, [0, -1, -2, 0]), 4.0))
    assert(almost_equal(expected(1, 6, 1, [0] * 10), 8.6))
    assert(almost_equal(expected(2, 6, 1, [0] * 10), 10.2))
