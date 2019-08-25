# https://py.checkio.org/mission/seven-segment/publications/flpo/python-3/digitf
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
    def digit(f):
        lit, broken = ({s.lower() for s in segs if f(s)} for segs in args)
        return sum(lit <= s <= (broken | lit) for s in segments)
    return digit(str.islower) * digit(str.isupper)
