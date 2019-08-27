import itertools


def is_iter(val):
    try:
        iter(val)
    except TypeError:
        return False
    return True


counter = 0
def completely_empty(val):
    print("===========")
    print(val)
    try:
        iter1 = iter(val)
    except TypeError:
        return False
    for it in iter1: print(it)
    global counter
    while True:
        counter += 1
        print(counter)
        if counter >=5: break
        completely_empty(iter1)
    return False
    # count = 0
    # for it in val:
    #     tp = type(it)
    #     if tp in [int]: return False
    #     if tp in [str]: return val == ''
    #     if tp in [list]:
    #         if len(it) != 0: return False
    #         count += 1
    # return len(val) == count


if __name__ == '__main__':
    # assert completely_empty([]) == True, "First"
    # assert completely_empty([1]) == False, "Second"
    # assert completely_empty([[]]) == True, "Third"
    # assert completely_empty([[],[]]) == True, "Forth"
    assert completely_empty([[[]]]) == True, "Fifth"
    # assert completely_empty([[],[1]]) == False, "Sixth"
    # assert completely_empty([0]) == False, "[0]"
    # assert completely_empty(['']) == True
    # assert completely_empty([[],[{'':'No WAY'}]]) == True
    print('Done')
