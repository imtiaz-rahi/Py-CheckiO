import re


def popular_words(text: str, words: list) -> dict:
    result = {}
    for word in words:
        regex = re.compile(r'\b%s\b' % word, re.IGNORECASE)
        result[word] = len(regex.findall(text))
    return result


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }

    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ["one", "two", "three"]) == {
        'one': 1,
        'two': 1,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
