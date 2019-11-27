def checkio(data):
    return data.pop() + checkio(data) if data else 0
