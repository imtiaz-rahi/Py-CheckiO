from string import ascii_lowercase as letters
checkio = lambda data: max(letters, key=data.lower().count)
