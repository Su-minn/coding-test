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

    # 1) Input Values
    ## Input R, C, T
    R, C, T = map(int, input().split())

    ## Input A_(r,c)
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
    print(board)

    # 2) Spread fine dust
    for nx, row in enumerate(board):
        for ny, cell in enumerate(row):
            ## If the cell has an air cleaner or is empty -> pass
            if cell == -1 or cell == 0:
                continue
            else:
                ## for the four directions
                spread_air = board[nx][ny] // 5
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    temp_x, temp_y = nx + dx, ny + dy
                    ## nx, ny is in the board, not air cleaner
                    if (0 <= temp_x <= R-1 and 0 <= temp_y <= C-1) and board[temp_x][temp_y] != -1:
                        board[nx][ny] -= spread_air
                        board[temp_x][temp_y] += spread_air

    # 3) Operate air cleaner
    answer = True

    print(board)

    return answer

# Input Test
solution()