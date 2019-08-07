# https://py.checkio.org/mission/count-consecutive-summers/publications/Phil15/python-3/4th-fast/?ordering=most_voted&filtering=all
# I proved on paper that what we want is equal the number of odd divisors of n.
def count_consecutive_summers(n):
    while not n % 2: n //= 2 # We first need to get rid of "even" part of n.
    # Then apply formula by searching prime numbers less than sqrt(n).
    # formula for sigma0 from https://en.wikipedia.org/wiki/Divisor_function#Formulas_at_prime_powers
    result, prime = 1, 3
    while 1 != n >= prime ** 2:
        count = 1
        while not n % prime:
            n //= prime
            count += 1
        result *= count
        prime += 2 # not always prime but is prime when it divides n.
    return result * (1, 2)[n != 1] # if n != 1 then n is prime and has 2 odd divisors.

if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")

