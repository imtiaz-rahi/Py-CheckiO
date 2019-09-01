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
