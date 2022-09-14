from collections import Counter


def solution(str1, str2):
    min_set, max_set = get_min_max_set(get_multi_set(str1), get_multi_set(str2))

    return int(calculate_jacard(min_set, max_set) * 65536)


def calculate_jacard(min_set, max_set):
    min_sum = sum(min_set.values())
    max_sum = sum(max_set.values())

    return min_sum / max_sum if max_sum != 0 else 1


def get_min_max_set(multi_set_1, multi_set_2):
    min_set = multi_set_1 & multi_set_2
    max_set = multi_set_1 | multi_set_2

    return min_set, max_set


def get_multi_set(s):
    multi_set = [
        s[idx : idx + 2].lower()
        for idx in range(len(s) - 1)
        if s[idx : idx + 2].isalpha()
    ]

    return Counter(multi_set)
