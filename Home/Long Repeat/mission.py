# https://stackoverflow.com/questions/30259981/given-a-string-find-out-the-highest-repeated-characters-count-in-python
def long_repeat(line):
    max_count = 0
    count = 0;
    last_ch = ""
    for ch in line:
        if ch == last_ch:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 1
            last_ch = ch

    return max_count if max_count > count else count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('abababa') == 1, "First"
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
