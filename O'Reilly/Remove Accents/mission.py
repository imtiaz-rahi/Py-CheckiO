import unicodedata as ud

def checkio(in_string):
    return ''.join(c for c in ud.normalize('NFD', in_string) if ud.category(c) != 'Mn')

if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
