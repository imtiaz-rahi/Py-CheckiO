# Code updated based on clear solution.
# https://py.checkio.org/mission/friendly-number/publications/Sim0000/python-3/first/
def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    # First decide on the exponent
    for e in range(len(powers)):
        if abs(number) < base ** (e + 1): break
    number /= base ** e
    number = round(number, decimals) if decimals else int(number)
    return f'{number:0.{decimals}f}{powers[e]}{suffix}'


if __name__ == '__main__':
    assert friendly_number(10 ** 32) == '100000000Y'
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12000000, decimals=3) == '12.000M', '12.000M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(-150, base=100, powers=['', 'd', 'D']) == '-1d'
    assert friendly_number(-155, base=100, decimals=1, powers=['', 'd', 'D']) == '-1.6d'
    assert friendly_number(255000000000, powers=['', 'k', 'M']) == '255000M'
