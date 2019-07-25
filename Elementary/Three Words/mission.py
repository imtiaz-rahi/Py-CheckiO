import re
def checkio(words: str) -> bool:
    count = 0
    for word in words.split(" "):
        if bool(re.search(r"[0-9]+", word)):
            count = 0
        else:
            count += 1
        if count is 3:
            return True
    return False

# Clear solution [https://py.checkio.org/mission/three-words/publications/veky/python-3/for-else]
#def checkio(words):
#    succ = 0
#    for word in words.split():
#        succ = (succ + 1) * word.isalpha()
#        if succ == 3: return True
#    else: return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    assert checkio("one two 3 four five 6 seven eight 9 ten eleven 12") == False
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
