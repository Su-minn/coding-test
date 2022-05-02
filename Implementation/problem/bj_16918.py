from jussuit_notes_ps.utils import *

## 문제 : 백준 16918번 - 봄버맨
## 링크 : https://www.acmicpc.net/problem/16918

## 풀이
### - 입력 : R(row), C(column), N(time) / (1 <= R, C, N <= 200) // A_(R,C)
### - 출력 : N 초 후, R 개의 줄에 격자판 상태
### - 시간 제한 : 2초
### - 메모리 제한 : 512MB

@time_check
def solution(*args, **kwargs):
    import sys
    import copy

    # 1) Input Values
    R, C, N = map(int, input().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(R)]
    time = [[1] * C for _ in range(R)]

    # Repeat N seconds
    for _ in range(2, N+1):

        ## Add one seconds
        for i in range(R):
            time[i] = list(map(lambda x: x + 1, time[i]))

        # 2) Add Bombs
        for nx, row in enumerate(board):
            for ny, cell in enumerate(row):
                if cell == '.':
                    board[nx][ny] = 'O'
                    time[nx][ny] = 0

        # 3) Bombs Explosion
        temp_board = copy.deepcopy(board)
        for nx, row in enumerate(temp_board):
            for ny, cell in enumerate(row):
                if cell == 'O' and time[nx][ny] == 3:
                    board[nx][ny] = '.'
                    ## For four directions
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        temp_x = nx + dx
                        temp_y = ny + dy
                        if 0 <= temp_x < R and 0 <= temp_y < C and temp_board[temp_x][temp_y] == 'O':
                            board[temp_x][temp_y] = '.'

    return board

# Input Test
board = solution()
for row in board:
    print(''.join(row))