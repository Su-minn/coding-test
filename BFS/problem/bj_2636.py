import queue
from jussuit_notes_ps.utils import *

## 문제 : 백준 2636번 - 치즈
## 링크 : https://www.acmicpc.net/problem/2636

## 풀이
### - 입력 : 세로(R), 가로(C) / (1 <= R, C <= 100) // A_(R, C) = 0(치즈 없는 칸) or 1(치즈 있는 칸)
### - 출력 : 치즈가 모두 녹아 없어지는데 걸리는 시간 / 녹기 한 시간 전 남아있는 치즈 조각 수
### - 시간 제한 : 1초
### - 메모리 제한 : 128MB

import sys
input = sys.stdin.readline
from collections import deque

# BFS function
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == False:
                if board[nx][ny] == 0: queue.append((nx, ny))
                else: board[nx][ny] = 0
                visited[nx][ny] = True

# 1) Input Value
R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
t = 0
num_cheese = sum(map(sum, board))
cheese_queue = deque([-1, num_cheese])

# 2) Repeat until cheese melts away
while cheese_queue[1] != 0:
    cheese_queue.popleft()
    visited = [[False] * C for _ in range(R)]
    bfs(0, 0)
    cheese_queue.append(sum(map(sum, board)))
    t += 1

# print answer
print(t)
print(cheese_queue[0])