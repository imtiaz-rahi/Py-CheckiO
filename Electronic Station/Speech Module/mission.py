FIRST_TEN = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    result = []
    hundreds = int(number / 100)
    if hundreds > 0:
        result.append(f"{FIRST_TEN[hundreds]} {HUNDRED}")
    number = number % 100
    tens = int(number / 10)
    if tens > 1:
        result.append(f"{OTHER_TENS[tens-2]} {FIRST_TEN[number%10]}")
    elif tens > 0:
        result.append(SECOND_TEN[number-10])
    else:
        result.append(FIRST_TEN[number%10])
    return ' '.join(result).rstrip()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
