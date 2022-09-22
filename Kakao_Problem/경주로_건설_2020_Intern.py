from heapq import heappush, heappop

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3


def solution(board):
    return get_min_cost_by_best_first_bfs(board)


def get_min_cost_by_best_first_bfs(board):
    move_to_dir = {(-1, 0): UP, (1, 0): DOWN, (0, -1): LEFT, (0, 1): RIGHT}
    is_arrived = False
    visited = [
        [[float("inf")] * len(board) for _ in range(len(board))]
        for _ in (UP, DOWN, LEFT, RIGHT)
    ]
    heap = []
    min_cost = float("inf")

    initialize_start_pos(heap, visited)

    while heap:
        cost, r, c, prev_dir = heappop(heap)

        if r == len(board[0]) - 1 and c == len(board[0]) - 1:
            if cost < min_cost:
                min_cost = cost
            is_arrived = True

        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + move[0], c + move[1]

            if (
                is_reachable_board(nr, nc, board)
                and visited[move_to_dir[move]][nr][nc] > cost
            ):  # valid condition and bound
                if is_arrived is True and cost > min_cost:  # bound
                    continue

                add_cost = 600 if prev_dir != (0, 0) and prev_dir != move else 100
                heappush(heap, [cost + add_cost, nr, nc, move])
                visited[move_to_dir[move]][nr][nc] = cost + add_cost

    return min_cost


def initialize_start_pos(heap, visited):
    heap.append([0, 0, 0, (0, 0)])

    for direction in (UP, DOWN, LEFT, RIGHT):
        visited[direction][0][0] = 0


def is_reachable_board(r, c, board):
    board_len = len(board[0])

    return 0 <= r < board_len and 0 <= c < board_len and board[r][c] == 0
