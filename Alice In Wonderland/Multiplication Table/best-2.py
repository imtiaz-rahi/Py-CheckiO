# https://py.checkio.org/mission/multiplication-table/publications/przemyslaw.daniel/python-3/5-liner-easy/
def checkio(a, b):
    result, k = 0, 2**b.bit_length()-1
    for i in map(int, bin(a)[2:]):
        result += (k*i & b)+(k*i | b)+(k*i ^ b)
    return result
