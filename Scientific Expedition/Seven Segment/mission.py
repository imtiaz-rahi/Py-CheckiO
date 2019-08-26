from itertools import combinations
NUMBERS = {
    '1': ['b', 'c'],
    '2': ['a', 'b', 'd', 'e', 'g'],
    '3': ['a', 'b', 'c', 'd', 'g'],
    '4': ['b', 'c', 'f', 'g'],
    '5': ['a', 'c', 'd', 'f', 'g'],
    '6': ['a', 'c', 'd', 'e', 'f', 'g'],
    '7': ['a', 'b', 'c'],
    '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    '9': ['a', 'b', 'c', 'd', 'f', 'g'],
    '0': ['a', 'b', 'c', 'd', 'e', 'f'],
}
lowers = {tuple(val): key for key, val in NUMBERS.items()}
uppers = {tuple([it.upper() for it in val]): key for key, val in NUMBERS.items()}


def get_num(lights):
    seg_upper = {it for it in lights if it.isupper()}
    if len(seg_upper) < 2 or len(lights - seg_upper) < 2: return None
    seg_lower = tuple(sorted(lights - seg_upper))
    try:
        return uppers[tuple(sorted(seg_upper))] + lowers[seg_lower]
    except KeyError:
        return None


def seven_segment(lit_seg, broken_seg):
    # Prepare all combination of items from broken_seg
    broken_list = [list(combinations(broken_seg, i)) for i in range(1, len(broken_seg))]
    # Flat the list of list of tuple
    broken_list = [item for sublist in broken_list for item in sublist]

    lit_seg = set(lit_seg)
    # Combine with lit_seg to get new combination of lighted segments
    full_set = [lit_seg | set(broken_seg)]
    for broken in broken_list:
        full_set.append(lit_seg | set(el for el in broken))
    if lit_seg:
        full_set.append(lit_seg)

    # Prepare list of numbers available from different combination of 7-segment display
    result = [get_num(lit_seg | item) for item in full_set]
    # Remove all None from the number list
    return len(list(filter(None, result)))
