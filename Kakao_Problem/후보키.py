# 문제 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/42890


def solution(relation):
    col_len = len(relation[0])
    col_sets = get_col_sets(col_len)
    unique_col_set = get_unique_key(col_sets, relation)
    candidate_key = get_candidate_key(unique_col_set)

    return len(candidate_key)


def get_unique_key(col_sets, relation):

    return [col_set for col_set in col_sets if check_uniqueness(col_set, relation)]


def get_candidate_key(unique_col_set):
    unique_col_set.sort(key=lambda x: len(x))
    candidate_key = []

    for col_set in unique_col_set:
        if all([len(set(key) - set(col_set)) for key in candidate_key]):
            candidate_key.append(col_set)

    return candidate_key


def get_col_sets(col_len):
    col_sets = []

    for mask in range(1, 1 << col_len):
        select_col = list(bin(mask)[2:].zfill(col_len))
        col_set = [
            col_idx for col, col_idx in zip(select_col, range(col_len)) if col == "1"
        ]
        col_sets.append(col_set)

    return col_sets


# itertools.combinations 모듈 이용
# def get_col_sets(col_len):
#     from itertools import combinations

#     col_sets = []
#     for r in range(1, col_len + 1):
#         col_sets += list(combinations(range(col_len), r))

#     return col_sets


def check_uniqueness(col_set, relation):
    col_projection = []

    for row in relation:
        col_projection.append(tuple([row[col] for col in col_set]))

    return len(col_projection) == len(set(col_projection))
