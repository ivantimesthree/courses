def missing_number(num_list, n):
    total_sum = n * (n + 1) // 2
    list_sum = sum(num_list)
    return total_sum - list_sum


def main():
    num_list = [1, 2, 3, 4, 6]
    n = 6
    missing = missing_number(num_list, n)
    print(f"The missing number is: {missing}")


if __name__ == "__main__":
    main()
