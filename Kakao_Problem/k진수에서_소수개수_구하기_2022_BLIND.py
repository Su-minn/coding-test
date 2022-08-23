# 문제 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/92335


from collections import deque
from math import sqrt


def solution(n, k):
    k_notation_num = convert_k_notation(n, k)
    prime_candidate = k_notation_num.split("0")
    prime_count = count_prime_number(prime_candidate)

    return prime_count


def is_prime(num):
    if num == 1:
        return False

    for r in range(2, int(sqrt(num)) + 1):
        if num % r == 0:
            return False

    return True


def count_prime_number(prime_candidate):
    count = 0

    for num in prime_candidate:
        if not num:
            continue

        if is_prime(int(num)):
            count += 1

    return count


def convert_k_notation(n, k):
    q, r = divmod(n, k)
    k_notation_list = deque([str(r)])

    while q != 0:
        q, r = divmod(q, k)
        k_notation_list.appendleft(str(r))

    return "".join(k_notation_list)
