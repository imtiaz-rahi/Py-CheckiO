import collections
from itertools import chain


def find_dups(data, val):
    return [k for k, v in data.items() if v == val]


def most_crucial(net, users):
    max_user = max(users, key=users.get)
    if len(find_dups(users, users[max_user])) == 1:
        return [max_user]
    # print(len(users.values()) == len(set(users.values())))
    # Create counter of user and their count in net
    network = collections.Counter([it for sub in net for it in sub])
    print(network)
    # check if multiple user has same count
    # if not len(network.values()) == len(set(network.values())):
    #     for k, v in network.items():
    #         network[k] = v * users[k]
    # print(network)
    return [max(network, key=network.get)]


if __name__ == '__main__':
    assert most_crucial([
        ["A", "B"],
        ["B", "C"],
        ["C", "D"]
    ], {
        "A": 100,
        "B": 1,
        "C": 97,
        "D": 1}) == ['A']

    assert most_crucial([
        ['A', 'B'],
        ['B', 'C']
    ], {
        'A': 10,
        'B': 10,
        'C': 10
    }) == ['B'], 'First'

    assert most_crucial([
        ['A', 'B']
    ], {
        'A': 20,
        'B': 10
    }) == ['A'], 'Second'

    assert most_crucial([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E']
    ], {
        'A': 0,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10
    }) == ['A'], 'Third'

    assert most_crucial([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 10,
        'D': 20
    }) == ['B'], 'Forth'

    print('Nobody expected that, but you did it! It is time to share it!')
