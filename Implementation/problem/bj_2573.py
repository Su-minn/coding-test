from jussuit_notes_ps.utils import *

## 문제 : 백준 2573번 - 빙산
## 링크 : https://www.acmicpc.net/problem/2573

## 풀이
### - 입력 : N (row), M (column) / (3 <= N, M <= 300) // A_(N, M) / (0 <= A_(N, M) <= 10)
### - 출력 : t (빙산이 분리되는 최초의 시간(년)) or 0 (빙산이 녹을 때까지 분리되지 않는 경우)
### - 시간 제한 : 1초
### - 메모리 제한 : 256MB

import sys
import copy
from collections import deque

# BFS function
def bfs(x, y):
    queue = deque([[x, y]])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and board[nx][ny] > 0:
                queue.append([nx, ny])
                visited[nx][ny] = True

    return 1

@time_check
def solution(time):
    # 2) The stage an iceberg melts
    temp_board = copy.deepcopy(board)
    for nx, row in enumerate(board):
        for ny, cell in enumerate(row):
            if cell != 0:
                # Check four directions
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    # if the direction is towards the sea
                    if (0 <= nx + dx <= N - 1) and (0 <= ny + dy <= M - 1) and temp_board[nx + dx][ny + dy] == 0:
                        if board[nx][ny] != 0: board[nx][ny] -= 1

    # Add one year
    time += 1

    # 3) Check whether the iceberg splits
    num_parts = 0
    for nx, row in enumerate(board):
        for ny, cell in enumerate(row):
            if cell != 0 and visited[nx][ny] == False:
                num_parts += bfs(nx, ny)

    return num_parts, time

# 1) Input values
N, M = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time = 0
num_parts = 1

while num_parts == 1:
    visited = [[False] * M for _ in range(N)]
    num_parts, time = solution(time)

if num_parts == 0:
    print(0)
else:
    print(time)
