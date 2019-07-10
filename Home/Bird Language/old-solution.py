VOWELS = "aeiouy"


def translate(phrase):
    idx = 0
    value = ""
    while idx < len(phrase):
        ch = phrase[idx]
        value += ch
        if ch == " ":
            idx += 1
        else:
            idx += 3 if ch in VOWELS else 2
    return value


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
