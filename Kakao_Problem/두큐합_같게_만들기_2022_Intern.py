from collections import deque


def solution(queue1, queue2):
    deque_1 = deque(queue1)
    deque_2 = deque(queue2)
    queue_len = len(queue1)

    is_found, count = check_same_sum(deque_1, deque_2, queue_len)

    return count if is_found is True else -1


def check_same_sum(deque_1, deque_2, queue_len):
    sum_1 = sum(deque_1)
    sum_2 = sum(deque_2)
    target_sum = (sum_1 + sum_2) // 2
    count = 0

    while count <= queue_len * 3:
        if sum_1 == target_sum:
            return (True, count)

        if sum_1 > sum_2:
            sum_1, sum_2 = pop_and_insert(deque_1, deque_2, sum_1, sum_2)
        else:
            sum_2, sum_1 = pop_and_insert(deque_2, deque_1, sum_2, sum_1)

        count += 1

    return (False, None)


def pop_and_insert(deque_pop, deque_insert, sum_pop, sum_insert):
    el = deque_pop.popleft()
    deque_insert.append(el)
    sum_pop -= el
    sum_insert += el

    return sum_pop, sum_insert
