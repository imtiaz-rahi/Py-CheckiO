# https://py.checkio.org/mission/friendly-number/publications/Sim0000/python-3/first/
def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    # At first, decompose the number to value and exponent.
    e = 0
    while e + 1 < len(powers) and abs(number) >= base ** (e + 1) : e += 1
    number /= base ** e
    # Then round it.
    number = round(number, decimals) if decimals else int(number)
    # At last, Format it.
    return '{:.0f}'.replace('0', str(decimals)).format(number) + powers[e] + suffix


if __name__ == '__main__':
    assert friendly_number(10**32) == '100000000Y'
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
