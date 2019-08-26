def to_encrypt(text, delta):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return "".join([alpha[(alpha.index(ch) + delta)%26] if ch != " " else " " for ch in text])


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
