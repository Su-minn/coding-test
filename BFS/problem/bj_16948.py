## 문제 : 백준 16948번 - 데스 나이트
## 링크 : https://www.acmicpc.net/problem/16948

## 풀이
### - 입력 : N (체스판의 크기) (5 <= N <= 200) / r1, c1, r2, c2
### - 출력 : (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수 / 이동할 수 없는 경우 -1
### - 시간 제한 : 2초
### - 메모리 제한 : 512MB

from collections import deque

# BFS
def bfs(r1, c1, r2, c2, visited, N):
    queue = deque([(r1, c1)])
    visited[r1][c1] = 0

    while queue:
        r, c = queue.popleft()

        if r == r2 and c == c2:
            return visited[r][c]
            
        for dr, dc in [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == False:
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    return -1


def solution():
    # Input Values
    N = int(input())
    visited = [[False] * N for _ in range(N)]
    r1, c1, r2, c2 = map(int, input().split())
    min_move = bfs(r1, c1, r2, c2, visited, N)
    return min_move


# Input Test
answer = solution()
print(answer)