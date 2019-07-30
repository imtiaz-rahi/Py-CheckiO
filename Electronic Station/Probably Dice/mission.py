# https://stackoverflow.com/questions/36134980/probability-of-t-total-eyes-when-throwing-n-dice-with-s-sides
import collections


def probability(dice_number, sides, target):
    prev = {0: 1}  # previous roll is 0 for first time
    for _ in range(dice_number):
        cur = collections.defaultdict(int)  # current probability
        for r, times in prev.items():
            for i in range(1, sides + 1):
                cur[r + i] += times
        prev = cur  # use this for the next iteration

    return round(cur[target] / sides ** dice_number, 4)


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    # assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    # assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    # assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    # assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    # assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    # assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
