import re


def checkio(data: str) -> bool:
    has_num = bool(re.search(r"[0-9]+", data))
    has_upp = bool(re.search(r"[A-Z]+", data))
    has_low = bool(re.search(r"[a-z]+", data))
    return len(data) >= 10 and has_num and has_low and has_upp


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
