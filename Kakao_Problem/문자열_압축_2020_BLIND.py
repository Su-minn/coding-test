def solution(s):
    min_length = 1

    for unit_len in range(1, len(s) // 2 + 1):
        min_length = get_min_len(s, unit_len, min_length)

    return min_length


def get_min_len(s, unit_len, min_length):
    count = 1
    length = 0
    prev_ch = s[:unit_len]
    compressed_ch = []

    for i in range(unit_len, len(s), unit_len):
        if min_length != 1 and length >= min_length:
            return min_length

        if prev_ch == s[i:i + unit_len]:
            count += 1
        else:
            length = update_count_and_ch(compressed_ch, count, length, prev_ch)
            count = 1
        prev_ch = s[i:i + unit_len]

    length = update_count_and_ch(compressed_ch, count, length, prev_ch)

    return min(length, min_length) if min_length != 1 else length


def update_count_and_ch(compressed_ch, count, length, prev_ch):
    length = update_compressed_ch(compressed_ch, length, ch=count) if count > 1 else length

    return update_compressed_ch(compressed_ch, length, ch=prev_ch)


def update_compressed_ch(compressed_ch, length, ch):
    compressed_ch.append(str(ch))

    return length + len(str(ch))
