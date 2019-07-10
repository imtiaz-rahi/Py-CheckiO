import numpy as np
import math

def minutes(time):
    h, m = time.split(":")
    m = int(h)*60+int(m)
    return m

def sun_angle(time):
    mins = minutes(time)
    if mins<minutes("6:00") or mins>minutes("18:00"):
        return "I don't see the sun!"
    array = np.arange(0, 181, 180/720)
    return (array[mins-minutes("6:00")])

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
