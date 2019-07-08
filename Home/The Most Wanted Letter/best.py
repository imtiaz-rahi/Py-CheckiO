import string


# Shortest solution
# checkio=lambda t:max(map(chr,range(97,123)),key=t.lower().count)

# Clearmost solution
def checkio(text):
    """
    We iterate through latin alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

#checkio = lambda text:max(string.ascii_lowercase, key=text.lower().count)

# Creative
# def checkio(text):
#     r = {c: text.lower().count(chr(c)) for c in range(97, 123)}
#     return chr(max(r, key=r.__getitem__ ))

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
