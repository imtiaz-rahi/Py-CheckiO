def flat_list(array):
    def flat_it(lst):
        for el in lst:
            if isinstance(el, (list, tuple)):
                yield from flat_it(el)
            else:
                yield el
    return list(flat_it(array))
