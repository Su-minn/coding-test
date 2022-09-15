def solution(p):
    collect_bracket = []
    answer = get_collect_bracket(p, collect_bracket)

    return answer


def get_collect_bracket(p, collect_bracket):
    if not p:
        return ""

    u, v = get_u_and_v(p)

    if is_collect_bracket(u):
        collect_bracket += list(u)
        get_collect_bracket(v, collect_bracket)
    else:
        collect_bracket.append("(")
        get_collect_bracket(v, collect_bracket)
        collect_bracket.append(")")
        collect_bracket += ["(" if ch == ")" else ")" for ch in u[1:-1]]

    return "".join(collect_bracket)


def get_u_and_v(p):
    left_bracket_num = 0
    right_bracket_num = 0

    for idx, ch in enumerate(p):
        if ch == "(":
            left_bracket_num += 1
        else:
            right_bracket_num += 1

        if left_bracket_num == right_bracket_num:
            u, v = p[: idx + 1], p[idx + 1 :]
            break

    return u, v


def is_collect_bracket(u):
    stack = [u[0]]

    for ch in u[1:]:
        if ch == "(":
            stack.append(ch)
        else:
            if not stack:
                return False

            stack.pop()

    return len(stack) == 0
