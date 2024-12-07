def max_value_key(data_dict):
    max_value_key = ["key_name", float("-inf")]
    for key, value in data_dict.items():
        if value > max_value_key[1]:
            max_value_key = [key, value]
    return max_value_key[0]


def main():
    data_dict = {"a": 5, "b": 9, "c": 2}
    print(max_value_key(data_dict))


if __name__ == "__main__":
    main()
