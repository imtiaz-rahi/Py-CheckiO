# https://py.checkio.org/mission/node-crucial/publications/przemyslaw.daniel/python-3/16-liner-almost-easy
def subnetworks(net, crush):
    result = {x: {x} for x in sum(net, []) if x not in crush}
    for a, b in net*len(net):
        if set(crush) & {a, b}: continue
        result[a] |= result[b] | {a, b}
        result[b] |= result[a] | {a, b}
    return {frozenset(x) for x in result.values()}

def most_crucial(net, users):
    result = {}
    for user in users.keys():
        value = users[user]
        for sub in subnetworks(net, user):
            value += sum([users[x] for x in sub])**2
        result[user] = value
    return [k for k, v in result.items() if v == min(result.values())]
