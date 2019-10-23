# https://py.checkio.org/forum/post/9298/sorted-function-explanation-please/
# https://py.checkio.org/forum/post/9342/got-stuck-on-sort-a-dict/
import re


def checkio1(text):
    text = text.lower()
    list1 = re.findall(r'[a-zA-Z]', text)
    set1 = set(list1)
    times = [list1.count(i) for i in set1]
    d = dict(zip(set1, times))
    d1 = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    return d1[0][0]


def checkio(text):
    text = str.lower(text).replace(' ', '')
    counter = [(char, text.count(char)) for char in set(text) if char.isalpha()]
    # Sort numbers (x[1]) in reverse order (highest first) and alphabets (x[0]) in natural ascending order
    # https://py.checkio.org/forum/post/9298/sorted-function-explanation-please/?#comment-40882
    counter.sort(key=lambda x: (-x[1], x[0]))
    return counter[0][0]


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    assert checkio("lorem ipsum dolor sit amet") == "m", "Should be m not o"
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
