def solution(play_time, adv_time, logs):
    play_time_array = [0] * (get_time_index(*parse_time(play_time)) + 1)

    accumulate_sum = get_accumulate_sum(logs, play_time_array)
    adv_length = get_time_index(*parse_time(adv_time))
    best_adv_time = get_best_adv_time(accumulate_sum, adv_length, play_time_array)

    return best_adv_time


def get_best_adv_time(accumulate_sum, adv_length, play_time_array):
    total_play_time = sum(accumulate_sum[:adv_length])
    max_total_play_time = total_play_time
    best_adv_time = get_time_from_index(0)

    for start_idx in range(1, len(play_time_array) - adv_length):
        end_idx = start_idx + adv_length - 1
        total_play_time += accumulate_sum[end_idx] - accumulate_sum[start_idx - 1]

        if total_play_time > max_total_play_time:
            max_total_play_time = total_play_time
            best_adv_time = get_time_from_index(start_idx)

    return best_adv_time


def get_accumulate_sum(logs, play_time_array):
    for log in logs:
        start_time, end_time = log.split("-")
        start_idx = get_time_index(*parse_time(start_time))
        end_idx = get_time_index(*parse_time(end_time))
        play_time_array[start_idx] += 1
        play_time_array[end_idx] -= 1

    for idx in range(len(play_time_array) - 1):
        play_time_array[idx + 1] += play_time_array[idx]

    return play_time_array


def get_time_index(h, m, s):
    return (60 * 60 * h) + (60 * m) + (s)


def get_time_from_index(index):
    result = []

    for _ in range(2):
        index, r = divmod(index, 60)
        result.append(r)

    result.append(index % 100)

    return ":".join(str(t).zfill(2) for t in reversed(result))


def parse_time(play_time):
    return [int(time) for time in play_time.split(":")]
