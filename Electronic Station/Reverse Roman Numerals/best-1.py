# https://py.checkio.org/mission/reverse-roman-numerals/publications/przemyslaw.daniel/python-3/based-on-best-roman-numerals-solution
def reverse_roman(n):
    result = 0
    for roman, arabic in zip('CM   CD   XC  XL  IX IV M     D    C    L   X   V  I'.split(),
                             (900, 400, 90, 40, 9, 4, 1000, 500, 100, 50, 10, 5, 1)):
        result += n.count(roman)*arabic
        n = n.replace(roman, '')
    return result
