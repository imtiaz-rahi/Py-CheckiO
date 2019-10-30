from itertools import chain


def check_connection(network, first, second):
    network = [it.split("-") for it in network]
    network = sorted(network, key=lambda x: first in x or second in x, reverse=True)
    relations = [first, second]
    for a, b in network:
        if a in relations or b in relations:
            print(f'{a}, {b}')
            relations.append(a)
            relations.append(b)
    print(relations)
    return True


# def check_connection(network, first, second):
#     network = [it.split("-") for it in network]
#     # Only keep the ones which have first or second
#     relations = [it for it in network if first in it or second in it]
#     print(relations)
#     # Flatten the relations
#     relations = list(chain.from_iterable(relations))
#     print(relations)
#     print(set(relations))
#     return len(set(relations)) == 3


if __name__ == '__main__':
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "dr101", "sscout") == False, "I don't know any scouts."
