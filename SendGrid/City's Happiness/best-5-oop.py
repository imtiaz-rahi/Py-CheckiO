# https://py.checkio.org/mission/node-crucial/publications/bsquare/python-3/elegant-oop-solution-ready-for-the-3-sendgrid-challenges/
class Connections(set):
    __BROKEN_NODE = frozenset('X')

    def __init__(self, connections):
        super().__init__(map(frozenset, connections))

    def nodes(self):
        return {node for connection in self for node in connection}

    def connected_node(self, name):
        return {node for connection in self for node in connection
                if name in connection and node != name}

    def connected_network(self, node, result):
        connected_nodes = self.connected_node(node) - self.__BROKEN_NODE - result
        result |= {node}
        for other in connected_nodes:
            result |= self.connected_network(other, result)

        return result

    def disconnect(self, nodes):
        broken_links = set()
        for connection in self:
            if nodes & connection:
                broken_links.add(connection - nodes | self.__BROKEN_NODE)

        self -= {connection for connection in self if nodes & connection}
        self |= broken_links

    def __str__(self):
        return '; '.join([f"({connection})" for connection in self])

def compute_importance(net, users, crushes, all_nodes):
    connections = Connections(net)
    connections.disconnect(set(crushes))

    network_seen = set()
    value = 0
    for node in all_nodes:
        if node in network_seen or not connections.connected_node(node):
            continue

        network = connections.connected_network(node, set())
        network_seen |= network
        value += (sum(value for user, value in users.items() if user in network))**2

    return value + sum(value for user, value in users.items() if user in crushes)

def most_crucial(net, users):
    all_nodes = {nodes for connection in net for nodes in connection}
    importances_map = {node: compute_importance(net, users, [node], all_nodes) for node in all_nodes}
    min_value = min(importances_map.values())
    return [node for node, value in importances_map.items() if value == min_value]


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
