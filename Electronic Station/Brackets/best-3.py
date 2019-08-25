# https://py.checkio.org/mission/brackets/publications/texom512/python-3/simple-and-only-5-lines
def checkio(str):
    str = ''.join([c for c in str if c in '()[]{}'])
    
    while any(b in str for b in ('()', '[]', '{}')):
        str = str.replace('()', '').replace('[]', '').replace('{}', '')

    return not str
