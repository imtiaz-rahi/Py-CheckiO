# https://py.checkio.org/mission/count-consecutive-summers/publications/Phil15/python-3/v3-count-odd-divisors/?ordering=most_voted&filtering=all
# Well I saw that what we want is equal to the number of odd divisors of n so...
count_consecutive_summers = lambda n: sum(not n%k for k in range(1, n+1, 2))

if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
