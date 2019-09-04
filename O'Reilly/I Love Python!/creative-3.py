# https://py.checkio.org/mission/i-love-python/publications/gyahun_dash/python-3/except-me-in-the-lie/
def i_hate(language):
    if language == 'Python':
        raise MemoryError(language)
    else:
        return 'I hate {}!'.format(language)

def i_love_python():
    try:
        return i_hate('Python')
    except MemoryError as me:
        return 'I love {}!'.format(me.args[0])
