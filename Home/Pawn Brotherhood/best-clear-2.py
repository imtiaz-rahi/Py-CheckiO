# https://py.checkio.org/mission/pawn-brotherhood/publications/slickLash/python-3/simple/?ordering=most_voted&filtering=choice
def safe_pawns(pawns):
    
    def is_safe(p):
        file, rank = ord(p[0]), int(p[-1])
        return (chr(file-1)+str(rank-1) in pawns or 
                chr(file+1)+str(rank-1) in pawns)
        
    return sum(is_safe(p) for p in pawns)
