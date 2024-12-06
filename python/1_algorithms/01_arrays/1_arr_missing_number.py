def missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum


def main():
    print(missing_number([1, 2, 3, 4, 5], 6))


if __name__ == "__main__":
    main()
