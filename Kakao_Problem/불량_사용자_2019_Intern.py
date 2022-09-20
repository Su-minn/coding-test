def solution(user_id, banned_id):
    global result

    result = []
    get_numbers_of_case(user_id, banned_id, [])

    return len({tuple(sorted(id_list)) for id_list in result})


def get_numbers_of_case(user_id, banned_id, id_list):
    if len(banned_id) == 0:
        result.append(id_list[:])

        return

    for bid in banned_id[:]:
        for uid in user_id[:]:
            if match_id(bid, uid):
                user_id.remove(uid)
                banned_id.remove(bid)
                get_numbers_of_case(user_id, banned_id, id_list + [uid])
                user_id.append(uid)
                banned_id.append(bid)

        return


def match_id(bid, uid):
    if len(bid) == len(uid):
        for bid_ch, uid_ch in zip(bid, uid):
            if not (bid_ch == uid_ch or bid_ch == "*"):
                return False
        return True

    return False
