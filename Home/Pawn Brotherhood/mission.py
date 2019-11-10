def safe_pawns(pawns: set) -> int:
    def is_friend(p):
        w, d = ord(p[0]), int(p[-1])
        return (chr(w - 1) + str(d - 1) in pawns or
                chr(w + 1) + str(d - 1) in pawns)

    return sum(is_friend(pn) for pn in pawns)
