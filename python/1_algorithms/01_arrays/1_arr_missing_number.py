def missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum


if __name__ == "__main__":
    print(missing_number([1, 2, 3, 4, 5], 6))
