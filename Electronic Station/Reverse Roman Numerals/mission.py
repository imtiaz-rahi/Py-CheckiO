def reverse_roman(roman_string):
    roms = ('CM', 'M',  'CD', 'D', 'XC', 'C', 'XL', 'L', 'IX', 'X', 'IV', 'V', 'I')
    ints = (900,  1000, 400, 500, 90,  100,   40,  50,   9,   10,    4,   5,    1)
    num = 0
    for i in range(len(roms)):
        count = roman_string.count(roms[i])
        if count > 0:
            roman_string = roman_string.replace(roms[i], "")
            num += ints[i] * count
    return num


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    # assert reverse_roman('CDXCIX') == 499, '499'
    # assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');
