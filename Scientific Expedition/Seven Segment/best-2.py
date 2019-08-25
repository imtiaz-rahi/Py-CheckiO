# https://py.checkio.org/mission/seven-segment/publications/flpo/python-3/for-f-in-strisupper-strislower/
segments = list(map(set, [
    'bc',
    'abged',
    'abgcd',
    'fbgc',
    'afgcd',
    'afgcde',
    'abc',
    'abcdefg',
    'abcdfg',
    'abcdef'
]))


def seven_segment(*args):
    r = 1
    for f in str.isupper, str.islower:
        lit, broken = ({s.lower() for s in segs if f(s)} for segs in args)
        r *= sum(lit <= s <= (broken | lit) for s in segments)
    return r
