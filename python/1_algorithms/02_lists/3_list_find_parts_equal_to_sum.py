def find_pairs_equal_to_sum(num_list, target_sum):
    found_pairs_indexes = []
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] == num_list[j]:  # Because the pairs have to be distinct
                continue
            elif num_list[i] + num_list[j] == target_sum:
                found_pairs_indexes.append([i, j])
    return found_pairs_indexes


def main():
    num_list = [2, 6, 3, 9, 11]
    target_sum = 9
    print(find_pairs_equal_to_sum(num_list, target_sum))


if __name__ == "__main__":
    main()
