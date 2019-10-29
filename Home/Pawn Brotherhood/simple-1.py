def safe_pawns(pawns: set) -> int:
    nb_safe = 0
    for p in pawns:
        col_def_1 = chr(ord(p[0]) - 1)
        col_def_2 = chr(ord(p[0]) + 1)
        row_def = str(int(p[1]) - 1)
        if (col_def_1 + row_def in pawns) or (col_def_2 + row_def in pawns):
            nb_safe += 1
    return nb_safe

def safe_pawns(pawns: set) -> int:
    result = 0
    for pawn in pawns:
        col, row = ord(pawn[0]), int(pawn[1])
        if chr(col-1)+str(row-1) in pawns or chr(col+1)+str(row-1) in pawns:
            result += 1
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
