# https://py.checkio.org/mission/flatten-list/publications/hypehr96/python-3/first/
def flat_list(array):
    try:
        return [int(array)]
    except:
        return sum(map(flat_list, array), [])

