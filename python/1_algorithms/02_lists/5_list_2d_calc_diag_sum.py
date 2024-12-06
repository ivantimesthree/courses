def diagonal_sum(matrix):
    diag_sum = 0
    for i in range(len(matrix)):
        diag_sum += matrix[i][i]
    return diag_sum


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(diagonal_sum(matrix))


if __name__ == "__main__":
    main()
