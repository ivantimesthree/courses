def contains_duplicate(nums_list):
    unique_items = []
    for x in nums_list:
        if x not in unique_items:
            unique_items.append(x)
        else:
            return True
    return False


def main():
    nums_list = [1, 2, 3, 2, 1]
    print(contains_duplicate(nums_list))


if __name__ == "__main__":
    main()
