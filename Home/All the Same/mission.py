from typing import List, Any


# https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
def all_the_same(elements: List[Any]) -> bool:
    return elements[1:] == elements[:-1]

# return elements == elements[1:] + elements[:1]


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
