# https://py.checkio.org/mission/roman-numerals/publications/MaikSchoepe/python-3/first/?ordering=most_voted&filtering=choice
def checkio(data):
    base = "I"*data
    
    base = base.replace("I"*5, "V")
    base = base.replace("V"*2, "X")
    base = base.replace("X"*5, "L")
    base = base.replace("L"*2, "C")
    base = base.replace("C"*5, "D")
    base = base.replace("D"*2, "M")
    
    base = base.replace("DCCCC", "CM")
    base = base.replace("CCCC", "CD")
    base = base.replace("LXXXX", "XC")
    base = base.replace("XXXX", "XL")
    base = base.replace("VIIII", "IX")
    base = base.replace("IIII", "IV")
    
    return base

