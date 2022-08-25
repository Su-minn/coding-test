# 문제 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/17683


def solution(m, musicinfos):
    play_records = get_play_record(musicinfos)
    title = get_music_title(m, play_records)

    return title


def get_music_title(m, play_records):
    m_list = parse_by_melody(m)
    candidate_title = []

    for title, record in play_records.items():
        if exists_melody(m_list, record):
            candidate_title.append((title, len(record)))

    if candidate_title:
        candidate_title.sort(key=lambda x: x[1], reverse=True)
        title = candidate_title[0][0]
    else:
        title = "(None)"

    return title


def exists_melody(m, record):
    idx = 0

    for idx in range(len(record)):
        if m == record[idx : idx + len(m)]:
            return True

    return False


def get_play_record(musicinfos):
    play_records = {}

    for musicinfo in musicinfos:
        start_time, end_time, title, records = musicinfo.split(",")
        record_time = (
            int(end_time.split(":")[0]) - int(start_time.split(":")[0])
        ) * 60 + (int(end_time.split(":")[1]) - int(start_time.split(":")[1]))
        records_list = parse_by_melody(records)
        play_records[title] = [
            records_list[idx % len(records_list)] for idx in range(record_time)
        ]

    return play_records


def parse_by_melody(records):
    idx = 0
    records_list = []

    for idx in range(len(records) - 1):
        if records[idx + 1] == "#":
            melody = records[idx : idx + 2]
        elif records[idx] == "#":
            continue
        else:
            melody = records[idx]

        records_list.append(melody)

    if records[-1] != "#":
        records_list.append(records[-1])

    return records_list
