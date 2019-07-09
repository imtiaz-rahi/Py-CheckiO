from datetime import timedelta

TIME_ANGLE_RATIO = 0.25 # 90 degree for 360 minutes of time


def sun_angle(time: str):
    sunrise = timedelta(hours=6, minutes=0)
    sunset = timedelta(hours=18, minutes=0)

    ar = time.split(":")
    now = timedelta(hours=int(ar[0]), minutes=int(ar[1]))
    angle = ((now - sunrise).total_seconds() / 60) * TIME_ANGLE_RATIO
    return angle if sunrise <= now <= sunset else "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("06:00") == 0
    assert sun_angle("18:00") == 180
    assert sun_angle("01:23") == "I don't see the sun!"
    assert sun_angle("00:00") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
