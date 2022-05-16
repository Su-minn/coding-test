## 문제 : 백준 16234번 - Problem Title
## 링크 : https://www.acmicpc.net/problem/16234

## 풀이
### - 입력 : N (NxN 땅) (1 =< N =< 50) / L, R (L 이상, R 이하 기준 인구) (1 =< L, R =< 50) / A_(r,c) (0 <= A_(r,c) <= 100)
### - 출력 : 인구 이동이 발생한 기간 (며칠 동안 발생하는 지)
### - 시간 제한 : 2초
### - 메모리 제한 : 512 MB

# BFS Function
def bfs(x, y):
    queue = deque([(x, y)])
    visitied[x][y] = True
    union = [(x, y)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visitied[nx][ny] == False \
            and L <= abs(board[x][y] - board[nx][ny]) <= R:
                queue.append((nx, ny))
                visitied[nx][ny] = True
                union.append((nx, ny))
    unions.append(union)

import sys
input = sys.stdin.readline
from collections import deque

# 1) Input Variables
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
t = 0
move = True

# 2) Population Migration
while move:
    unions = []
    visitied = [[False] * N for _ in range(N)]

    # Check Union
    for nx, row in enumerate(board):
        for ny, cell in enumerate(row):
            if visitied[nx][ny] == False:
                bfs(nx, ny)
    
    # Polulation Migration
    if all(map(lambda x: len(x) == 1, unions)):
        move = False
        break
    else:
        for union in unions:
            if len(union) != 1:
                sum_union = sum([board[x][y] for x, y in union])
                for x, y in union:
                    board[x][y] = int(sum_union / len(union))
    
    t += 1

print(t)