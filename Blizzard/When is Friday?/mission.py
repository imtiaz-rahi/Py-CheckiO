from datetime import datetime

def friday(day):
    # Monday is 4 days away from Friday. Add an extra week to handle Sat and Sun
    return (11 - datetime.strptime(day, '%d.%m.%Y').weekday()) % 7

if __name__ == '__main__':
    assert friday('11.11.1111') == 6
    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
