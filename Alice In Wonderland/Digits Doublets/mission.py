# https://py.checkio.org/blog/digit-doublets-review/
# https://www.christianpeccei.com/doublets-in-python/
# https://www.blackgate.net/blog/doublet-solver-for-python/
# NOT MY CODE
def f(l, c, u):
    if l[-1] in c: return c
    s = [f(l, c + [x], u | {x}) for x in set(l) - u if sum(str(c[-1])[i] == str(x)[i] for i in (0, 1, 2)) == 2]
    return min(s, key=len) if s else [1] * 99


checkio = lambda l: f(l, [l[0]], {l[0]})

if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"
