def remove_duplicates(nums_list):
    new_list = []
    for x in nums_list:
        if x not in new_list:
            new_list.append(x)
    return new_list


def main():
    nums_list = [1, 1, 2, 2, 3, 4, 5]
    print(remove_duplicates(nums_list))


if __name__ == "__main__":
    main()
