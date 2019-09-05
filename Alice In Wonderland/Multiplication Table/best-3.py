# https://py.checkio.org/mission/multiplication-table/publications/brubru777/python-3/formula-with-explanation/
def checkio(first, second):
    '''Returns the result of "Stephan's multiplication" as defined in the problem'''
    first_bin = bin(first)[2:]
    ones = first_bin.count('1')
    zeroes = len(first_bin) - ones
    all_ones = 2 ** (len(bin(second)) - 2) - 1
    
    # Computation details
    # and_sum = zeroes * 0      + ones * second
    # or_sum  = zeroes * second + ones * all_ones
    # xor_sum = zeroes * second + ones * (all_ones ^ second)
    # 
    # Since n + (all_ones ^ n) = n for any number n, we get
    return (zeroes * second + ones * all_ones) * 2
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
