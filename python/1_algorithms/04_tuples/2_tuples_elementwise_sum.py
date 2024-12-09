def tuple_elementwise_sum(tuple_1, tuple_2):
    result = tuple(tuple_1[i] + tuple_2[i] for i in range(len(tuple_1)))
    return result


def main():
    tuple_1 = (1, 2, 3)
    tuple_2 = (4, 5, 6)
    output_tuple = tuple_elementwise_sum(tuple_1, tuple_2)
    print(output_tuple)


if __name__ == "__main__":
    main()
