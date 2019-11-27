def verify_anagrams(first_word, second_word):
    letters = lambda x: "".join(sorted(x.lower())).strip()
    return letters(first_word) == letters(second_word)


if __name__ == '__main__':
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
