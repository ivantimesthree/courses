def merge_dicts(dict_1, dict_2):
    for key, value in dict_2.items():
        if key in dict_1.keys():
            dict_1[key] += value
        else:
            dict_1[key] = value
    return dict_1


def main():
    dict_1 = {"a": 1, "b": 2, "c": 3}
    dict_2 = {"b": 3, "c": 4, "d": 5}
    print(merge_dicts(dict_1, dict_2))


if __name__ == "__main__":
    main()
