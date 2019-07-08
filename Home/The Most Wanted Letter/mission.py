import collections
import re

def check_equal(lst: list) -> bool:
    return lst[1:] == lst[:-1]


def create_list(data: iter) -> list:
    lst = []
    for d in data:
        lst.append(d)
    return lst

def checkio(text: str) -> str:
    az = collections.defaultdict(int)
    for ch in text.lower():
        if re.match(r'[^a-z]', ch): continue
        az[ch] += 1

    lst = sorted(az, key=az.get, reverse=True)
    if check_equal(create_list(az.values())):
        lst = sorted(lst)
    return lst[0]


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
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
