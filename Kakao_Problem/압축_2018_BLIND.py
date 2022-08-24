# 문제 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/17684


def solution(msg):
    answer = []
    lzw_dict = {chr(alpha): idx for idx, alpha in enumerate(range(65, 91), start=1)}
    idx = 0

    while idx < len(msg):
        dict_index, w_len = get_dict_index_and_w_len(lzw_dict, msg, idx)
        answer.append(dict_index)
        idx += w_len

    return answer


def get_dict_index_and_w_len(lzw_dict, msg, idx):
    for word_len in range(1, len(msg) + 1 - idx):
        current_word = msg[idx : idx + word_len]

        if current_word in lzw_dict:
            dict_index = lzw_dict[current_word]
        else:
            register_dict(current_word, lzw_dict)

            return (dict_index, len(current_word) - 1)

    return (dict_index, len(current_word))


def register_dict(current_word, lzw_dict):
    next_index = len(lzw_dict) + 1
    lzw_dict[current_word] = next_index
