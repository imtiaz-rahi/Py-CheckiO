# https://py.checkio.org/mission/pawn-brotherhood/publications/Tarty/python-3/intersection
def safe_pawns(pawns):
    safe = lambda s: {chr(ord(s[0]) - 1) + str(int(s[1]) - 1),
        chr(ord(s[0]) + 1) + str(int(s[1]) - 1)}

    return sum([bool(set(pawns).intersection(safe(p))) for p in pawns ])
