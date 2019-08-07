# https://www.geeksforgeeks.org/count-ways-express-number-sum-consecutive-numbers/
# http://codeforces.com/blog/entry/53763
# Python program to count number of ways to express N as sum of consecutive numbers.


def count_consecutive_summers(total):
    # constraint on values of L gives us the time Complexity as O(N^0.5)
    count = 0
    num = 1
    while num * (num + 1) < 2 * total:
        a = (1.0 * total - (num * (num + 1)) / 2) / (num + 1)
        if a - int(a) == 0.0:
            count += 1
        num += 1
    return count + 1


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))
    print(count_consecutive_summers(99))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
