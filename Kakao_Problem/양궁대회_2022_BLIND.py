# 문제 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/92342


def solution(n, info):
    max_score = 0

    for num in range(0, 1024):
        bit_mask = list(map(int, bin(num)[2:].zfill(10)))
        ryan_hit = [
            (apeeach_hit + 1) * is_ryan_hit
            for apeeach_hit, is_ryan_hit in zip(info[:-1], bit_mask)
        ]

        if n - sum(ryan_hit) >= 0:
            ryan_hit += [n - sum(ryan_hit)]
        else:
            continue

        score_diff = get_score_diff(info, ryan_hit)
        if max_score < score_diff:
            max_score = score_diff
            ryan_hit_answer = ryan_hit
        elif score_diff != 0 and max_score == score_diff:
            ryan_hit_answer = (
                ryan_hit
                if has_lower_score(ryan_hit, ryan_hit_answer)
                else ryan_hit_answer
            )

    if max_score == 0:
        return [-1]

    return ryan_hit_answer


def has_lower_score(ryan_hit, ryan_hit_answer):
    if not ryan_hit_answer:
        return True

    for prev_ryan, ryan in zip(ryan_hit_answer[::-1], ryan_hit[::-1]):
        if ryan > prev_ryan:
            return True
        elif prev_ryan > ryan:
            return False


def get_score_diff(info, ryan_hit):
    apeeach_score = 0
    ryan_score = 0
    score = 10

    for apeeach, ryan in zip(info, ryan_hit):
        if apeeach != 0 and apeeach >= ryan:
            apeeach_score += score
        elif ryan > apeeach:
            ryan_score += score

        score -= 1

    return ryan_score - apeeach_score
