from string import ascii_lowercase as ascii


def to_encrypt(text, delta):
    return ''.join([ascii[(ascii.index(char) + delta) % len(ascii)] if char in ascii else char for char in text])

