# https://py.checkio.org/mission/most-wanted-letter-2/publications/veky/python-3/just-use-a-counter/
import collections

def most_wanted(text):
    count = collections.Counter(filter(str.isalpha, text.casefold()))
    return [char for char, freq in count.items() if freq == max(count.values())]
