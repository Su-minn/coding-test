## 문제 : 백준 1389번 - 케빈 베이컨의 6단계 법칙
## 링크 : https://www.acmicpc.net/problem/1389

## 풀이

import sys
from collections import deque

# BFS 함수 정의
def bfs(start):
    kevin = [0] * (N + 1)
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                kevin[i] = kevin[v] + 1
    return sum(kevin)

# 유저의 수 N, 친구 관계의  수 M
N, M = map(int, input().split())

# graph
graph = [[] for _ in range(N+1)]

# M 번 반복하며 graph 에 관계 추가
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

# 중복 제거
graph = [list(set(i)) for i in graph]

# BFS 진행
temp = list(map(bfs, range(1, N+1)))
ans = temp.index(min(temp)) + 1

print(ans)