def solution(places):
    return [check_dist_rule(place) for place in places]


def check_dist_rule(place):
    for row_idx, row in enumerate(place):
        for col_idx, cell in enumerate(row):
            if cell == "P":
                visited = [[False] * 5 for _ in range(5)]
                if not check_dist_rule_by_dfs(row_idx, col_idx, place, visited):
                    return 0

    return 1


def check_dist_rule_by_dfs(r, c, place, visited, dist=0):
    if place[r][c] == "P" and dist != 0:
        return 0
    elif dist == 2:
        return 1

    visited[r][c] = True
    comply_rule = 1

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc

        if is_promising(nr, nc, place, visited):
            comply_rule = check_dist_rule_by_dfs(nr, nc, place, visited, dist + 1)
            if comply_rule == 0:
                break

    return comply_rule


def is_promising(r, c, place, visited):
    return (
        0 <= r < len(place)
        and 0 <= c < len(place[0])
        and place[r][c] != "X"
        and visited[r][c] is False
    )
