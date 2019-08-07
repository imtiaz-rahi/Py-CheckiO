# https://py.checkio.org/mission/count-consecutive-summers/publications/Ylliw/python-3/second-version-even-faster-can-someone-be-faster

count_consecutive_summers=lambda n:sum([n%b*2==b-b%2*b for b in range(1,int((2*n)**.5)+1)])
"""
Is this really working?
Yes it is, it's one of the shortest code to solve the problem and
it's doing it very efficiently as well

2nd version
-----------
How does it work:
sum from p to p+a when p and a are integers is (2p+a)*(a+1)/2
so n=(2p+a)*(a+1)/2
so 2p+a=2n/(a+1)
finally p=(2n-a-a^2)(2*(a+1))
replacing a+1 with b
p=(2n-b(b-1))/2b
and we know that p should b an integer, which means that 2n-b(b-1)%(2b)==0
or 2n%(2b)==b(b-1)%(2b)
Left part can be reduce to n%b*2
Right part can be reduce to (b-1)%2*b which can be written b-b%2*b for 2 characters less

Values for a are from a=0 (sum of a single value) to a=0.5*(-1+sqrt(1+8*n)) when we have the lonest sum of numbers
This value does not make a nice 'golf' code, but 0.5*(-1+sqrt(1+8*n)) is just slightly smaller than sqrt(2n)
for n=1 000 000, this means that the program will evaluate a up to 1414 instead of 1413, acceptable trade off for a shorter code :)
Values for b are therefore from 1 to sqrt(2n)+1

2nd version uses:
- b in place of a+1 for a lot of save characters
- modulo instead of int(x)==x to define if x is integer, greatly save chars but it's much faster (20-30%)

It was a great exerice so found a way to solve it for both code size and speed
"""


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")

