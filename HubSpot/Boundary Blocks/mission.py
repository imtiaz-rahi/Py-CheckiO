from typing import List, Tuple, Iterable


def boundary_blocks(grid: List[str]) -> Iterable[Tuple[int]]:

    return []


if __name__ == '__main__':
    assert set(boundary_blocks(['..X',
                                '.X.',
                                'X..'])) == {(0, 2), (1, 1), (2, 0)}, '#1 3x3'
    assert set(boundary_blocks(['...',
                                '.X.',
                                'X..'])) == set(), '#2 3x3'
    assert set(boundary_blocks(['X.X.',
                                '.X..',
                                '..X.',
                                '....'])) == {(0, 0), (0, 2), (1, 1)}, '#3 4x4'

    print('The local tests are done. Click on "Check" for more real tests.')