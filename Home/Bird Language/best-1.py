# https://py.checkio.org/mission/bird-language/publications/StefanPochmann/python-3/vek/
import re

def translate(phrase):
    return re.sub(r'(\w)\1?.', r'\1', phrase)


if __name__ == '__main__':
    print(translate("hieeelalaooo"))
    print(translate("hieelalaooooo"))
    #assert translate("hieeelalaooo") == "hello", "Hi!"
