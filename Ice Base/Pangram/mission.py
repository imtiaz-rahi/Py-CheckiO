import string

def check_pangram(text):
    return set(text.lower()) >= set(string.ascii_lowercase)
