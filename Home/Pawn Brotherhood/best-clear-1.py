# https://py.checkio.org/mission/pawn-brotherhood/publications/Kerulen/python-3/first/?ordering=most_voted&filtering=choice
def safe_pawns(pawns):
    answer = 0
    for pawn in pawns :
        if chr(ord(pawn[0])-1)+str(int(pawn[1])-1) in pawns or chr(ord(pawn[0])+1)+str(int(pawn[1])-1) in pawns : answer +=1
    return answer

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
