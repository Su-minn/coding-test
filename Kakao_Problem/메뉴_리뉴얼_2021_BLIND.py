from itertools import combinations
from collections import Counter


def solution(orders, course):
    course_table = get_course_table(orders, course)
    best_course = get_best_course(course_table, course)

    return get_answer(best_course)


def get_answer(best_course):
    answer = []

    for count, menu in best_course.values():
        if count < 2:
            continue
        answer.extend(menu)

    return sorted(answer)


def get_best_course(course_table, course):
    best_course = {k: [1, []] for k in course}

    for course_comb, count in course_table.items():
        if best_course[len(course_comb)][0] < count:
            best_course[len(course_comb)][0] = count
            best_course[len(course_comb)][1] = ["".join(course_comb)]
        elif best_course[len(course_comb)][0] == count:
            best_course[len(course_comb)][1].append("".join(course_comb))

    return best_course


def get_course_table(orders, course):
    course_table = Counter()

    for order in orders:
        for num in course:
            course_table.update(combinations(sorted(order), num))

    return course_table
