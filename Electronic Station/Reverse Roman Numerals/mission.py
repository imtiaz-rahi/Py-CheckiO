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
