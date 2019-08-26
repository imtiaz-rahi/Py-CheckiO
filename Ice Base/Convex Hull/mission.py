from scipy.spatial.qhull import ConvexHull


def checkio(data):
    hull = ConvexHull(data)
    vertices = list(hull.vertices[1:])
    vertices.append(hull.vertices[0])
    return list(reversed(vertices))


if __name__ == '__main__':
    # assert checkio(
    #     [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
    # ) == [4, 5, 6, 0, 1, 2, 3], "First example"
    assert checkio(
        [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
    ) == [1, 0, 6, 3, 5, 2], "Second example"
