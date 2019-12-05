# https://py.checkio.org/mission/double-substring/publications/Tinus_Trotyl/python-3/first/share/a5aa8875feb9da03651b851e44e62c87/


def double_substring(line):
    for ln in range(len(line)-1, 0, -1):
        print(ln)
        for i in range(len(line) - ln + 1):
            print(f'i={i}')
            if line.count(line[i:i+ln]) > 1: return ln
    return 0


if __name__ == '__main__':
    # assert double_substring('aaaa') == 2, "First"
    # assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
