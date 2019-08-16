# https://py.checkio.org/mission/roman-numerals/publications/MaikSchoepe/python-3/first/?ordering=most_voted&filtering=choice
def checkio(data):
    rs = (("I"*5, "V"),
          ("V"*2, "X"),
          ("X"*5, "L"),
          ("L"*2, "C"),
          ("C"*5, "D"),
          ("D"*2, "M"),
          ("DCCCC", "CM"),
          ("CCCC",  "CD"),
          ("LXXXX", "XC"),
          ("XXXX",  "XL"),
          ("VIIII", "IX"),
          ("IIII",  "IV"))

    base = "I" * data
    for r in rs:
        base = base.replace(*r)

    return base


if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    #assert checkio(76) == 'LXXVI', '76'
    #assert checkio(499) == 'CDXCIX', '499'
    #assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    #print('Done! Go Check!')
