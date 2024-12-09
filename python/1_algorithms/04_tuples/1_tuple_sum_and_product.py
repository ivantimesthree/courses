def sum_product(input_tuple):
    tuple_sum = 0
    tuple_product = 1
    for x in input_tuple:
        tuple_sum += x
        tuple_product *= x
    return tuple_sum, tuple_product


def main():
    input_tuple = (1, 2, 3, 4)
    sum_result, product_result = sum_product(input_tuple)
    print(sum_result, product_result)


if __name__ == "__main__":
    main()
