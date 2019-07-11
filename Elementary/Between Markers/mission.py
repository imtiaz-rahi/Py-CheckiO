def between_markers(text: str, begin: str, end: str) -> str:
    a, b, l = text.find(begin), text.find(end), len(begin)
    val = [text[a+l:b], text[a+l:], text[:b], text]
    #print(val)
    #print("pos: " + str(2 * (a<0)+(b<0)))
    return val[2 * (a<0)+(b<0)]

# https://py.checkio.org/blog/using-regular-expressions-in-python/
# https://py.checkio.org/mission/between-markers/publications/przemyslaw.daniel/python-3/3-liner-find-only
def between_markers1(txt, begin, end):
    a, b, c = txt.find(begin), txt.find(end), len(begin)
    return [txt[a+c:b], txt[a+c:], txt[:b], txt][2*(a<0)+(b<0)]

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
