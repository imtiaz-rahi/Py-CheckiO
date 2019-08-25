def checkio(expression):
    opening, closing = tuple('({['), tuple(')}]')
    # bracket dict looks like this; {'(': ')', '{': '}', '[': ']'}
    bracket = dict(zip(opening, closing))
    queue = []
    for letter in expression:
        if letter in opening:
            # Add the closing bracket of the opening found in queue to check later
            queue.append(bracket[letter])
        elif letter in closing:
            # This closing bracket must match the one in queue
            if not queue or letter != queue.pop():
                # otherwise it is unbalanced
                return False
    return True if not queue else False


if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("({[3]})-[4/(3*{1001-1000}*3)/4]") == True, "Big problem"
