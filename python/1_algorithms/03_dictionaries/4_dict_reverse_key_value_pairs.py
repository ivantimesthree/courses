def reverse_dict(data_dict):
    return {v: k for k, v in data_dict.items()}


def main():
    data_dict = {"a": 1, "b": 2, "c": 3}
    print(reverse_dict(data_dict))


if __name__ == "__main__":
    main()
