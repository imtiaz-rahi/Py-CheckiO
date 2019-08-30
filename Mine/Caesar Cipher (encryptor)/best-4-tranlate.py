def to_encrypt(text, delta):
     alpha='abcdefghijklmnopqrstuvwxyz'
     return text.translate(str.maketrans(alpha, alpha[delta:]+alpha[:delta]))
