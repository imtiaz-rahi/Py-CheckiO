# https://py.checkio.org/mission/triangle-angles/publications/PositronicLlama/python-3/trigonometry/?ordering=most_voted&filtering=all
"""Return the interior angles of a triangle."""
import math

def checkio(a, b, c):
    """
    Return the interior angles of a triangle in ascending order as a list.
    
    Return [0, 0, 0] if the side lengths a, b, c cannot form a triangle.
    """
    a, b, c = sorted((a, b, c))
    if a + b <= c:
        return [0, 0, 0]

    a2, b2, c2 = a**2, b**2, c**2
    angles = (math.acos((a2+b2-c2) / (2*a*b)),
              math.acos((a2+c2-b2) / (2*a*c)),
              math.acos((b2+c2-a2) / (2*b*c)))

    return list(sorted(round(math.degrees(a)) for a in angles))

if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
