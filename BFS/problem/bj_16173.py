## 문제 : 백준 16173번 - 점프왕 쩰리 (small)
## 링크 : https://www.acmicpc.net/problem/1706

## 풀이

from collections import deque

# N 입력
N = int(input())

# board 입력
board = [list(map(int, input().split())) for _ in range(N)]

# 방문 여부 list 생성
visited = [[False] * N for _ in range(N)]

# bfs 함수 정의
def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    # 방문 처리
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        # 오른쪽 방향 or 아래 방향으로만 이동
        for dx, dy in [(1, 0), (0, 1)]:
            nx = x + dx * board[x][y]
            ny = y + dy * board[x][y]

            # 유효성 검사
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1 and visited[nx][ny] == False:
                # 해당 위치의 board 값이 -1 이면 'HaruHaru' 출력
                if board[nx][ny] == -1:
                    return 'HaruHaru'
                else:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    # 도달할 수 없는 경우
    return 'Hing'

result = bfs(0, 0)
print(result)