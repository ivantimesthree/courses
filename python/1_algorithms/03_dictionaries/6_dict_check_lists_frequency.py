def check_same_frequency(list_1, list_2):
    return counted_elements(list_1) == counted_elements(list_2)


def counted_elements(data_list):
    counted = {}
    for x in data_list:
        if x not in counted.keys():
            counted[x] = 1
        else:
            counted[x] += 1
    return counted


def main():
    list_1 = [1, 2, 3, 2, 1]
    list_2 = [3, 1, 2, 1, 3]
    print(check_same_frequency(list_1, list_2))


if __name__ == "__main__":
    main()
