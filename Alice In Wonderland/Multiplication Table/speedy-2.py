checkio = lambda first, second: sum(sum(int(''.join([str(eval(a+operand+b)) for b in format(second, 'b')]),2)
                                                                            for a in format(first, 'b'))
                                                                            for operand in ['&','|','^'])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
