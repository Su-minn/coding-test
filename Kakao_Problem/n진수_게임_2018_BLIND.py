# 문제 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/17687


from collections import deque


def solution(n, t, m, p):
    answer_list = []
    start_idx = p - 1
    last_idx = start_idx + m * (t - 1)

    n_notation_str = get_n_notation_str(n, last_idx)

    for num in n_notation_str[start_idx : (last_idx + 1) : m]:
        answer_list.append(num)

    return "".join(answer_list)


def get_n_notation_str(n, last_idx):
    n_notaiton_list = []
    num = 0

    while len(n_notaiton_list) <= last_idx:
        n_notaiton_list.append(convert_n_notation(num, n))
        num += 1

    return "".join(n_notaiton_list)


def convert_n_notation(num, n):    
    BASE = "0123456789ABCDEF"
    
    q = num
    k_notation_list = deque([])
    
    while q != 0:
        q, r = divmod(q, n)
        k_notation_list.appendleft(BASE[r])
    
    return "".join(k_notation_list) if k_notation_list else "0"
