import re


def cut_sentence(line, length):
    if len(line) <= length:
        return line

    result = line[:length]
    last_item = re.findall(r"\b\w+\b", result).pop()
    if last_item not in re.findall(r"\b\w+\b", line):
        result = result.replace(last_item, "")
    return result.strip() + "..."


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert cut_sentence("Hi my name is Alex", 1) == "...", "First"
    assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    #assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    #assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    #assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    #assert cut_sentence("Hi my name is Alex", 10) == "Hi my name...", "Fifth"
    #assert cut_sentence("Hi my name is Alex", 11) == "Hi my name...", "Sixth"
    print('Done! Do you like it? Go Check it!')
