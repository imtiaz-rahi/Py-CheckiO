# https://py.checkio.org/mission/roman-numerals/publications/veky/python-3/enum/?ordering=most_voted&filtering=choice
from enum import Enum

class Roman(Enum):
    M  = 1000
    CM = 900
    D  = 500
    CD = 400
    C  = 100
    XC = 90
    L  = 50
    XL = 40
    X  = 10
    IX = 9
    V  = 5
    IV = 4
    I  = 1

    @classmethod
    def encode(cls, n):
        for numeral in cls:
            rep, n = divmod(n, numeral.value)
            yield numeral.name * rep

    def __str__(self):
        return ''.join(self.encode(self.value))
        
        
if __name__ == "__main__":
    print(Roman.encode(23))

            # def __str__(self):
    #     return self.encode(self.value)

# if __name__ == "__main__":
#     print("Roman numeral")
#     print("".join(Roman.encode(23)))
