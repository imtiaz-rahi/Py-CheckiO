def count_consecutive_summers(num):
    result = []
    for it in reversed(range(1, int(num/2))):
        sums = 0
        lst = []
        for i in reversed(range(1, it+1)):
            sums += i
            lst.append(i)
            if sums == num:
                result.append(lst)
            if sums >= num:
                break
    print(result)
    return len(result) + 1


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(99))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert count_consecutive_summers(42) == 4
    # assert count_consecutive_summers(99) == 6
    # assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
