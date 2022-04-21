## 문제 : 백준 2589번 - 보물섬
## 링크 : https://www.acmicpc.net/problem/2589

## 풀이

import sys
from collections import deque

# H, W 입력
H, W = map(int, input().split())

# H x W board 생성 및 입력
board = [list(sys.stdin.readline().strip()) for _ in range(H)]

visited = [[False] * W for _ in range(H)]

# bfs 함수 정의
def bfs(x, y):
    # queue 에 시작 좌표 삽입
    queue = deque([])
    t = 0
    max_time = 0
    queue.append([x, y, t])
    visited[x][y] = True

    # queue 에 값이 없을 때 까지 반복
    while queue:
        x, y, t = queue.popleft()

        # 상, 하, 좌, 우 좌표 확인
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            # (1) 탐색 좌표 nx, ny 가 유효하지 않거나, (2) 이미 방문한 좌표인 경우, (3) W (바다) 인경우 pass
            if not (0 <= nx < H and 0 <= ny < W) or visited[nx][ny] == True or board[nx][ny] == 'W':
                continue
            # queue 에 해당 좌표 삽입
            queue.append((nx, ny, t+1))
            # 해당 좌표 방문 처리
            visited[nx][ny] = True
            # time 최대값 갱신
            if t + 1 > max_time:
                max_time = t + 1

    return max_time

time = []
for x in range(H):
    for y in range(W):
        # 방문 여부 초기화 진행
        visited = [[False] * W for _ in range(H)]
        # 해당 좌표가 육지인 경우 탐색 진행
        if board[x][y] == 'L':
            t = bfs(x, y)
            time.append(t)

result = max(time)
print(result)