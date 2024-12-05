import numpy as np

arr = np.array(
    [
        [11, 15, 10, 6],
        [10, 14, 11, 5],
        [12, 17, 12, 8],
        [15, 18, 14, 9],
    ]
)


def access_elements(arr, row_index, col_index):
    if row_index >= len(arr) or col_index >= len(arr[0]):
        print("ERROR: Incorrect index.")
    else:
        print(arr[row_index][col_index])


def traverse_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j])


def linear_search(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == target:
                return f"The target is located at: {i, j}"
    return "The element is now found"


if __name__ == "__main__":
    # access_elements(arr, 1, 1)
    # traverse_array(arr)
    print(linear_search(arr, 6))
    pass
