# https://py.checkio.org/mission/friendly-number/publications/veky/python-3/decimal-ftw/
def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=('',)+tuple('kMGTPEZY')):
    """Format a number as friendly text, using common suffixes."""
    import decimal
    number = decimal.Decimal(number)
    for pw in powers:
        if abs(number) < base: break
        number /= base
    else: number *= base
    val = "{:.{}f}".format(number, decimals) if decimals else str(int(number))
    return val + pw + suffix
