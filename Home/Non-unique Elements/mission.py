# https://thispointer.com/python-how-to-convert-a-list-to-dictionary/
# https://stackoverflow.com/questions/29218750/what-is-the-best-way-to-remove-a-dictionary-item-by-value-in-python
# https://stackoverflow.com/questions/36268749/remove-multiple-items-from-a-python-list-in-just-one-statement
# https://py.checkio.org/blog/arrays-for-python/
def checkio(data: list) -> list:
    # Create dict with data.items as keys and their count as value
    result = {it: data.count(it) for it in data}
    # Keep only the unique elements (count == 1) in the dict
    result = {key: val for key, val in result.items() if val == 1}
    # Remove the unique elements from list and return it
    return [el for el in data if el not in result.keys()]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
