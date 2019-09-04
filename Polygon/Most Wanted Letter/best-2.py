# https://py.checkio.org/mission/most-wanted-letter-2/publications/Chocolater/python-3/first/
from string import ascii_lowercase as alphabet


def most_wanted(text: str) -> str:
    return [letter for letter in alphabet if text.lower().count(letter) ==
            max(text.lower().count(max_letter) for max_letter in alphabet)]
