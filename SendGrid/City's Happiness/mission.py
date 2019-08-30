import collections


def find_dups(data, val):
    return [k for k, v in data.items() if v == val]


def most_crucial(net, users):
    max_user = max(users, key=users.get)
    # Check whether multiple node has same max user count
    top_user = find_dups(users, users[max_user])
    if len(top_user) == 1:
        return top_user

    # Prepare count of node presence in the network
    net_count = collections.Counter([it for sub in net for it in sub])
    top_nets = find_dups(net_count, net_count[max(net_count, key=net_count.get)])
    if len(top_nets) == 1:
        return top_nets
    return sorted(set(top_user) & set(top_nets))


if __name__ == '__main__':

    assert most_crucial([["A", "B"], ["B", "C"], ["C", "A"]],
                        {"A": 10, "C": 10, "B": 5}) == ['A', 'C']

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
