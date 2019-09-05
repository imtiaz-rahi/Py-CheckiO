def checkio(a, b):
    c = bin(a)[2:]
    return 2 * (c.count("1") * (2**(len(bin(b)) - 2) - 1) + c.count("0") * b)
