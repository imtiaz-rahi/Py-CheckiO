from itertools import chain


def connected_nodes(net, crushes):
    for crashed in crushes:
        for n in net:
            if crashed in n:
                n.remove(crashed)
    # Return only the networks nodes which are still fully connected
    return [n for n in net if len(n) == 2]


def disconnected_users(net, users, source, crushes):
    if source in crushes: return sum(users.values())
    net = set(chain.from_iterable(connected_nodes(net, crushes)))
    if len(net) == 0 or source not in net:
        del users[source]
    else:
        for it in net: del users[it]
    return sum(users.values())


if __name__ == '__main__':
    assert disconnected_users([
        ["A", "B"],
        ["B", "C"],
        ["C", "D"]
    ], {
        "A": 10,
        "C": 30,
        "B": 20,
        "D": 40
    }, "A", ["A"]) == 100, "Test 4/4: Nobody will get a mesage if node that sends emails is crushed"

    assert disconnected_users([
        ["A", "B"],
        ["B", "C"],
        ["C", "D"]
    ], {
        "A": 10,
        "C": 30,
        "B": 20,
        "D": 40
    }, "A", ["B"]) == 90, "Test 1/1: Users from node B(20), C(30) and D(40) didn't get a message"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    }, 'A', ['C']) == 70, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    }, 'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    }, 'C', ['A']) == 50, "Third"

    print('Done. Try to check now. There are a lot of other tests')
