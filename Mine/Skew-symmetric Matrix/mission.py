# https://www.programiz.com/python-programming/examples/transpose-matrix
def checkio(matrix):
    return matrix == [[-matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# for i in range(len(matrix)):
#    # iterate through columns
#    for j in range(len(matrix[0])):
#        result[j][i] = matrix[i][j]

if __name__ == '__main__':
    assert checkio([
        [0, 1, 2, 3, 4],
        [-1, 0, 5, 6, 7],
        [-2, -5, 0, 8, 9],
        [-3, -6, -8, 0, 0],
        [-4, -7, -9, 0, 0]]) == True, "4th example"

    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!");
