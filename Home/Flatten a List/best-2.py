# https://py.checkio.org/mission/flatten-list/publications/nickie/python-3/ignalions-twist/
def flat_list(l):
    r = []
    def f(l):
        for i in l:
            r.append(i) if type(i) is int else f(i)
    f(l)
    return r
