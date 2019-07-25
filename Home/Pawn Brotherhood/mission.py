def valid_pos(ch: str, dg: int) -> bool:
    return ch + str(dg) if ch.isalpha() and ch < 'i' and 0 < dg < 9 else None


def friends(pawn: str) -> set:
    ns = set()
    (w, d) = pawn

    ns.add(valid_pos(chr(ord(w) + 1), int(d) - 1))
    ns.add(valid_pos(chr(ord(w) - 1), int(d) - 1))
    return set(filter(lambda el: el is not None, ns))


def safe_pawns(pawns: set) -> int:
    count = 0
    for pawn in pawns:
        count += bool(friends(pawn) & pawns)
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
