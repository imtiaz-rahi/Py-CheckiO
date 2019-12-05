# https://py.checkio.org/mission/double-substring/publications/StefanPochmann/python-3/4-problems-1-solution/share/af71a294ba1313bced37c36f80d834aa/

def longest_substring(string, predicate):
    n = len(string)
    for length in range(n, -1, -1):
        for start in range(n - length + 1):
            substring = string[start:start + length]
            if predicate(substring):
                return substring


def repeat_inside(line):
    return longest_substring(line, lambda s: s in (s + s)[1:-1])


def non_repeat(line):
    return longest_substring(line, lambda s: len(s) == len(set(s)))


def long_repeat(line):
    return len(longest_substring(line, lambda s: len(set(s)) < 2))


def double_substring(line):
    return len(longest_substring(line, lambda s: line.count(s) > 1 or not s))


if __name__ == '__main__':
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
