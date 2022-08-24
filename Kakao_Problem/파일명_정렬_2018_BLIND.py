# 문제 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/17686


def solution(files):
    files.sort(key=lambda x: (parse_head(x), parse_number(x)))

    return files


def parse_head(file):
    head_end_idx = get_head_end_idx(file)

    return "".join([ch.lower() for ch in file[: head_end_idx + 1]])


def parse_number(file):
    number = []
    head_end_idx = get_head_end_idx(file)

    for ch in file[head_end_idx + 1 : head_end_idx + 6]:
        if not ch.isdigit():
            break

        number.append(ch)

    return int("".join(number))


def get_head_end_idx(file):
    end_idx = 0

    for ch in file[1:]:
        if ch.isdigit():
            return end_idx

        end_idx += 1

    return end_idx
