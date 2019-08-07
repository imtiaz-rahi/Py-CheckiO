def checkio(number: int) -> int:
    return len([i for i in str(bin(number)) if i == "1"])
