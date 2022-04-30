from jussuit_notes_ps.utils import *

## 문제 : 백준 17144번 - 미세먼지 안녕!
## 링크 : https://www.acmicpc.net/problem/17144

## 풀이
### - 입력 : R (row), C (column) (6 <= R, C <= 50) / T (time) (1 <= T <= 1000)
### - 출력 : T초 후 남아있는 전체 미세먼지 양
### - 시간 제한 : 1초
### - 메모리 제한 : 512 MB

@time_check
def solution(*args, **kwargs):
    import sys
    import copy

    # 1) Input Values
    ## Input R, C, T
    R, C, T = map(int, input().split())

    ## Input A_(r,c)
    board = []
    up_cleaner = -1

    for idx, _ in enumerate(range(R)):
        row = list(map(int, sys.stdin.readline().split()))
        if row[0] == -1:
            if up_cleaner == -1: up_cleaner, down_cleaner = idx, idx + 1

        board.append(row)

    # During time T
    for _ in range(T):
        # 2) Spread fine dust
        temp_board = copy.deepcopy(board)

        for nx, row in enumerate(board):
            for ny, cell in enumerate(row):
                ## If the cell has an air cleaner or is empty -> pass
                if cell == -1 or cell == 0:
                    continue
                else:
                    ## for the four directions
                    spread_air = temp_board[nx][ny] // 5
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        temp_x, temp_y = nx + dx, ny + dy
                        ## nx, ny is in the board, not air cleaner
                        if (0 <= temp_x <= R-1 and 0 <= temp_y <= C-1) and board[temp_x][temp_y] != -1:
                            board[nx][ny] -= spread_air
                            board[temp_x][temp_y] += spread_air

        # 3) Operate air cleaner
        temp_board = copy.deepcopy(board)
        ## shift down & up
        ### rotate upside
        for i in range(1, up_cleaner + 1):
            ## shift down
            ### if the air cleaner is not in below
            if i != 1: board[up_cleaner - i + 1][0] = temp_board[up_cleaner - i][0]
            ## shift up
            board[i - 1][C - 1] = temp_board[i][C - 1]

        ### rotate downside
        for i in range(1, R - down_cleaner):
            ## shift up
            ### if the air cleaner is not in below
            if i != 1: board[down_cleaner + i - 1][0] = temp_board[down_cleaner + i][0]
            ## shift down
            board[R - i][C - 1] = temp_board[R - i - 1][C - 1]

        ## shift right & left
        for i in range(1, C):
            ## shift right
            if i == 1: board[up_cleaner][i], board[down_cleaner][i] = 0, 0
            else: board[up_cleaner][i], board[down_cleaner][i] = temp_board[up_cleaner][i - 1], temp_board[down_cleaner][i - 1]
            ## shift left
            board[R - 1][i - 1], board[0][i - 1] = temp_board[R - 1][i], temp_board[0][i]

    answer = sum(map(sum, board)) + 2
    return answer

# Input Test
print(solution())
