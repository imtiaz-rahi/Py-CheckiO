from math import factorial

def permutation_index(numbers: tuple)->int:
    rs = []
    sorted_num = sorted(numbers)
    for i, n in enumerate(numbers):
        if i == len(numbers) - 1: continue
        rs.append(sorted_num.index(n) * factorial(len(numbers) - i -1))
        sorted_num.remove(n)
    return sum(rs) + 1
