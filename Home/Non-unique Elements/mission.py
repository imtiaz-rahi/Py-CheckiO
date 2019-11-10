def checkio(data: list) -> list:
    # Create dict with data.items as keys and their count as value
    result = {it: data.count(it) for it in data}
    # Return the elements which have count more than 1
    return [el for el in data if result[el] > 1]
