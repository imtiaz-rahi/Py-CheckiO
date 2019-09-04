# https://py.checkio.org/mission/i-love-python/publications/Sim0000/python-3/decorator/
def love(func):
    def wrapper():
        return "I love {}!".format(func())
    return wrapper

@love
def i_love_python():
    return "Python"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
