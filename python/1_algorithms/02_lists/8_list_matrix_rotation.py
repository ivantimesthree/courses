# Rotate 90 degrees clockwise
def rotate_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        matrix[i] = list(reversed(matrix[i]))

    return matrix


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_matrix(matrix))


if __name__ == "__main__":
    main()
