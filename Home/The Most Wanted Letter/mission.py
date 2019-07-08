import collections
import re


def create_list(data: iter) -> list:
    lst = []
    for d in data:
        lst.append(d)
    return lst


def count(lst, x):
    count = 0
    for ele in lst:
        if ele == x:
            count += 1
    return count


def checkio(text: str) -> str:
    az = collections.defaultdict(int)
    for ch in text.lower():
        if re.match(r'[^a-z]', ch): continue
        az[ch] += 1

    # Reverse sort the dict based on value
    lst = sorted(az, key=az.get, reverse=True)
    # Take only the alphabets which has the max occurrence
    vals = create_list(az.values())
    if max(vals) > min(vals):
        lst = lst[:count(vals, max(vals))]
    # Sort key (alphabets) list and return the first item
    return sorted(lst)[0]


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
