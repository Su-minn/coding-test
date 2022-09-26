from collections import deque


def solution(board):
    state_space_set = get_state_space_set(board)

    return get_min_distance_by_bfs(board, state_space_set)


def get_min_distance_by_bfs(board, state_space_set):
    LEFT, RIGHT, UP, DOWN = (0, -1), (0, 1), (-1, 0), (1, 0)

    start_pos = ((0, 0), (0, 1))
    queue = deque([(start_pos, 0)])
    state_space_set[start_pos] = True

    while queue:
        robot_pos, dist = queue.popleft()
        first_pos, second_pos = robot_pos

        if any(is_finish(board, pos) for pos in (first_pos, second_pos)):
            return dist

        is_horizon = is_horizontal(first_pos, second_pos)
        rotate_dir_1, rotate_dir_3 = ((1, -1), (-1, 1)) if is_horizon else ((-1, 1), (1, -1))
        rotate_dir_2, rotate_dir_4 = (-1, -1), (1, 1)
        for move in (
                [shift(direction) for direction in (LEFT, RIGHT, UP, DOWN)] +
                [rotate(pos, axis, is_horizon, board) for pos, axis
                 in ((rotate_dir_1, 0), (rotate_dir_2, 0), (rotate_dir_3, 1), (rotate_dir_4, 1))]):
            first_next_pos, second_next_pos = move((first_pos, second_pos))

            if (first_next_pos, second_next_pos) == (-1, -1):
                continue

            if is_in_board(board, first_next_pos, second_next_pos) and state_space_set[
                tuple(sorted((first_next_pos, second_next_pos)))] is False and not is_wall(board,
                                                                                           first_next_pos,
                                                                                           second_next_pos):
                state_space_set[tuple(sorted((first_next_pos, second_next_pos)))] = True
                queue.append((tuple(sorted((first_next_pos, second_next_pos))), dist + 1))


def is_finish(board, pos):
    return pos[0] == len(board) - 1 and pos[1] == len(board) - 1


def is_wall(board, first_pos, second_pos):
    return board[first_pos[0]][first_pos[1]] == 1 or board[second_pos[0]][second_pos[1]] == 1


def is_in_board(board, first_pos, second_pos):
    return all(map(lambda x: 0 <= x < len(board), first_pos + second_pos))


def is_horizontal(first_pos, second_pos):
    return first_pos[0] == second_pos[0]


def rotate(direction, axis, is_horizontal, board):
    def rotate_robot(robot_pos):
        first_pos_x, first_pos_y = robot_pos[0]
        second_pos_x, second_pos_y = robot_pos[1]
        if axis == 0:
            second_pos_x += direction[0]
            second_pos_y += direction[1]

            if is_horizontal and (not is_in_board(board, (second_pos_x, second_pos_y + 1), ()) or board[second_pos_x][
                second_pos_y + 1] == 1):
                return -1, -1
            elif not is_horizontal and (
                    not is_in_board(board, (second_pos_x + 1, second_pos_y), ()) or board[second_pos_x + 1][
                second_pos_y] == 1):
                return -1, -1
        else:
            first_pos_x += direction[0]
            first_pos_y += direction[1]

            if is_horizontal and (not is_in_board(board, (first_pos_x, first_pos_y - 1), ()) or board[first_pos_x][
                first_pos_y - 1] == 1):
                return -1, -1
            elif not is_horizontal and (
                    not is_in_board(board, (first_pos_x - 1, first_pos_y), ()) or board[first_pos_x - 1][
                first_pos_y] == 1):
                return -1, -1

        return (first_pos_x, first_pos_y), (second_pos_x, second_pos_y)

    return rotate_robot


def shift(direction):
    def shift_robot(robot_pos):
        first_pos_x, first_pos_y = robot_pos[0]
        second_pos_x, second_pos_y = robot_pos[1]
        first_pos_x += direction[0]
        second_pos_x += direction[0]
        first_pos_y += direction[1]
        second_pos_y += direction[1]

        return (first_pos_x, first_pos_y), (second_pos_x, second_pos_y)

    return shift_robot


def get_state_space_set(board):
    state_space_set = {}

    for row_idx in range(0, len(board)):
        state_space_set.update(
            {((row_idx, col_idx), (row_idx, col_idx + 1)): False for col_idx in range(0, len(board) - 1)})

    for col_idx in range(0, len(board)):
        state_space_set.update(
            {((row_idx, col_idx), (row_idx + 1, col_idx)): False for row_idx in range(0, len(board) - 1)})

    return state_space_set
