def subnetworks(net, crushes):
    isolated = []
    for crushed in crushes:
        for n in net:
            if crushed in n:
                n.remove(crushed)
                if len(n) == 0:
                    net.remove(n)
                    continue
                isolated.append(n[0])

    # Check whether any of the items in isolated are connected to another node in net
    for lonely in isolated:
        for n in net:
            if len(n) == 2 and lonely in n:
                net.remove([lonely])
    return len(net)


if __name__ == '__main__':
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']) == 2, "First"
    assert subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']) == 3, "Second"
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')
