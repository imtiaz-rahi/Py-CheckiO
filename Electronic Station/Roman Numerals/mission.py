# https://py.checkio.org/mission/roman-numerals/publications/StefanPochmann/python-3/short-and-clear/
def checkio(data):
    ints = (1000, 900,  500, 400, 100,  90,   50,  40,   10,   9,    5,   4,    1)
    nums = ('M',  'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = []
    for arabic, roman in zip(ints, nums):
        result.append(data // arabic * roman)
        data %= arabic
    return ''.join(result)


if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
