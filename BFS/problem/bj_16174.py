## 문제 : 백준 16174번 - 점프왕 쩰리 (Large)
## 링크 : https://www.acmicpc.net/problem/16174

## 풀이
### - 입력 : N (게임 구역의 크기) (2 <= N <= 64) / A_(r, c) (게임판 구역(맵)) (0 <= A_(r, c) <= 100)
### - 출력 : 끝 점 도달 가능하면 "HaruHaru", 도달 불가능하면 "Hing" 출력
### - 시간 제한 : 2초
### - 메모리 제한 : 128MB

from collections import deque
import sys
input = sys.stdin.readline

# BFS
def bfs(board, visited, N):
    queue = deque([[0, 0]])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        jump_num = board[x][y]
        
        # Reach the winning point
        if jump_num == -1:
            return True
        for dx, dy in [(jump_num, 0), (0, jump_num)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return False


def solution():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    if bfs(board, visited, N):
        print("HaruHaru")
    else:
        print("Hing")

# Input Test
solution()