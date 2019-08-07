# https://py.checkio.org/mission/count-consecutive-summers/publications/Sim0000/python-3/first/?ordering=most_voted&filtering=all
def count_consecutive_summers(num):
    # s + (s + 1) + (s + 2) + ... + (s + n)
    # = (n + 1) * s + n * (n + 1) / 2 = num
    # s = (num - n * (n + 1) / 2) / (n + 1)
    # we need denominator of s is divisible by n + 1
    count = 0
    for n in range(0, num): # we move n
        d = num - n * (n + 1) // 2 # calculate denominator
        if d <= 0: break
        if d % (n + 1) == 0: # s is integer?
            count += 1
    return count



if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
