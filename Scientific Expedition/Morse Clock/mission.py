def checkio(time_string: str) -> str:
    time_string = " ".join(":".join(it.zfill(2) for it in time_string.split(":")))
    result = ""
    mins = [2, 8, 14]
    hour_passed = False
    for i, it in enumerate(time_string):
        if it == ":":
            hour_passed = True
        fill = 3 if hour_passed else 2
        if i in mins:
            fill = 4
        if it.isdigit():
            it = bin(int(it))[2:].zfill(fill).replace("1", "-").replace("0", ".")
        result += it
    return result


if __name__ == '__main__':
    print("Example:")
    print(checkio("10:37:49"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")
