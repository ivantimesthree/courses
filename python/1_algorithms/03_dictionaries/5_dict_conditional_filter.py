def filter_dict(data_dict, condition):
    return {k: v for k, v in data_dict.items() if condition(k, v)}


def main():
    data_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
    filtered_dict = filter_dict(data_dict, lambda k, v: v % 2 == 0)
    print(filtered_dict)


if __name__ == "__main__":
    main()
