def solution(m, n, board):
    tr_board = [list(col) for col in zip(*board)]
    n, m = m, n
    total_block_num = 0

    while True:
        is_4_block = find_4_block(m, n, tr_board)
        block_num = count_block_num(is_4_block)

        if block_num == 0:
            break

        total_block_num += block_num
        move_board(m, n, is_4_block, tr_board)

    return total_block_num


def move_board(m, n, is_4_block, board):
    for nr in range(m):
        non_block_num = is_4_block[nr].count(True) + board[nr].count(-1)
        board[nr] = [-1] * non_block_num + [
            board[nr][nc]
            for nc in range(n)
            if is_4_block[nr][nc] == False and board[nr][nc] != -1
        ]


def count_block_num(is_4_block):
    return sum(map(sum, is_4_block))


def find_4_block(m, n, board):
    is_4_block = [[False] * n for _ in range(m)]

    for r, row_blocks in enumerate(board[:-1]):
        for c, _ in enumerate(row_blocks[:-1]):
            if (
                board[r][c] != -1
                and board[r][c]
                == board[r][c + 1]
                == board[r + 1][c]
                == board[r + 1][c + 1]
            ):
                mark_is_4_block(r, c, is_4_block)

    return is_4_block


def mark_is_4_block(row_idx, col_idx, is_4_block):
    for i, j in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        is_4_block[row_idx + i][col_idx + j] = True
