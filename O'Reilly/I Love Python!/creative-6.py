from re import findall
from random import choice

def i_love_python():
    """
        Why do I love Python?
    """
    return ' '.join([                 # It's a fusion of:
        "i".upper(),                  # your growth as a programmer,
        'Dreadful Flying Glove'[-4:], # it has All You Need ...
        findall('P.*?n',"Monty Python's Flying Circus")[0] # ... if you know how to find,
        + choice('!!!!!!!!!!!!!!!')]) # and many other excellent things!

if __name__ == '__main__':
    assert i_love_python() == "I love Python!"
