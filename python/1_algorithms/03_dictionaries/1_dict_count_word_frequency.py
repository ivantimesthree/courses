def count_word_frequency(words):
    words_dict = {}
    for x in words:
        if x not in words_dict.keys():
            words_dict[x] = 1
        else:
            words_dict[x] += 1
    return words_dict


def main():
    words = ["apple", "orange", "banana", "apple", "orange", "apple"]
    print(count_word_frequency(words))


if __name__ == "__main__":
    main()
