from numpy.polynomial.polynomial import polypow


def probability(dice_number, sides, target):
    """
    Using numpy polynomial
    The number of ways to obtain x as a sum of n s-sided dice
    is given by the coefficients of the polynomial:

    f(x) = (x + x^2 + ... + x^s)^n
    """

    # power series (note that the power series starts from x^1, therefore
    # the first coefficient is zero)
    powers = [0] + [1] * sides
    # f(x) polynomial, computed used polypow in numpy
    poly = polypow(powers, dice_number)
    return poly[target] / sides ** dice_number if target < len(poly) else 0


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
