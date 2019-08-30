def encrypt(char, delta):
    if char == " ":
        return " "
    else:
        return chr(((ord(char) - 97 + delta) % 26) + 97)

def to_encrypt(text, delta):
    return ("").join([encrypt(x, delta) for x in text])
