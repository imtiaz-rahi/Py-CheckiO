# https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
# https://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists
def flat_list(array):

    def flat_it(lst):
        for el in lst:
            if isinstance(el, (list, tuple)):
                yield from flat_it(el)
            else:
                yield el

    return list(flat_it(array))


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
