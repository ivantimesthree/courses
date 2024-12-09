def common_elements(tuple_1, tuple_2):
    return tuple(x for x in tuple_1 if x in tuple_2)


def main():
    tuple_1 = (1, 2, 3, 4, 5)
    tuple_2 = (4, 5, 6, 7, 8)
    output_tuple = common_elements(tuple_1, tuple_2)
    print(output_tuple)


if __name__ == "__main__":
    main()
