def max_product(nums_list):
    first_max = 0
    second_max = 0
    for num in nums_list:
        if num >= first_max:
            second_max = first_max
            first_max = num
    return first_max * second_max


def main():
    nums_list = [1, 7, 3, 4, 9, 5]
    print(max_product(nums_list))


if __name__ == "__main__":
    main()
