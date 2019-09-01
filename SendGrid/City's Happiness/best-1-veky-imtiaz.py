# https://py.checkio.org/mission/node-crucial/publications/veky/python-3/imtiazrahis-pythonified/
from collections import Counter


def most_crucial(net, users):
    # {'user': {'A': 10, 'C': 10, 'B': 5}, 'net': Counter({'A': 2, 'B': 2, 'C': 2})}
    top = dict(user=users, net=Counter(sum(net, [])))
    for name, bunch in top.items():
        max_value = max(bunch.values())
        keys = {key for key, value in bunch.items() if value == max_value}
        if len(keys) == 1: return list(keys)
        top[name] = keys
    return sorted(top['user'] & top['net'])


if __name__ == '__main__':

    assert most_crucial([["A", "B"], ["B", "C"], ["C", "A"]],
                        {"A": 10, "C": 10, "B": 5}) == ['A', 'C']

    # assert most_crucial([
    #     ["A", "B"],
    #     ["B", "C"],
    #     ["C", "D"]
    # ], {
    #     "A": 100,
    #     "B": 1,
    #     "C": 97,
    #     "D": 1}) == ['A']
    #
    # assert most_crucial([
    #     ['A', 'B'],
    #     ['B', 'C']
    # ], {
    #     'A': 10,
    #     'B': 10,
    #     'C': 10
    # }) == ['B'], 'First'
    #
    # assert most_crucial([
    #     ['A', 'B']
    # ], {
    #     'A': 20,
    #     'B': 10
    # }) == ['A'], 'Second'
    #
    # assert most_crucial([
    #     ['A', 'B'],
    #     ['A', 'C'],
    #     ['A', 'D'],
    #     ['A', 'E']
    # ], {
    #     'A': 0,
    #     'B': 10,
    #     'C': 10,
    #     'D': 10,
    #     'E': 10
    # }) == ['A'], 'Third'
    #
    # assert most_crucial([
    #     ['A', 'B'],
    #     ['B', 'C'],
    #     ['C', 'D']
    # ], {
    #     'A': 10,
    #     'B': 20,
    #     'C': 10,
    #     'D': 20
    # }) == ['B'], 'Forth'

    print('Nobody expected that, but you did it! It is time to share it!')
