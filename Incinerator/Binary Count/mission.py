def checkio(number: int) -> int:
    return len([i for i in str(bin(number)) if i == "1"])

# return bin(number).count('1')
# return "{0:b}".format(number).count('1')
# checkio=lambda x:bin(x).count('1')
# return str(bin(number))[2:].count('1')


