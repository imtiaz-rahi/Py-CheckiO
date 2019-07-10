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

# Best, clear solution https://py.checkio.org/mission/non-unique-elements/publications/eiji/python-3/eiji
# But slower, O(N^2)
# return [i for i in data if data.count(i) > 1]
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# or remove elements from original list (but it's bad practice for many real cases)
# Loop over original list

# Nice O(n) solution. Runs roughly 80x faster than the data.count(n) solution for a 1000 element list.
# https://py.checkio.org/mission/non-unique-elements/publications/v0id/python-3/first
# from collections import Counter
# def checkio(data):
#     counter = Counter(data)
#     return [item for item in data if counter[item] > 1

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    assert list(checkio(list(range(100000))+[0])) == [0, 0], "big list"
    print("It is all good. Let's check it now")
