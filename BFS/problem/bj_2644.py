## 문제 : 백준 2644번 - 촌수 계산
## 링크 : https://www.acmicpc.net/problem/2644

## 풀이

import sys
from collections import deque

# BFS 함수 정의
def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                answer[i] = answer[v] + 1

# 전체 사람 수 n
n = int(input())

# 촌 수 계산 대상
a, b = map(int, input().split())

# 관계의 개수 m
m = int(input())

# graph
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = [0] * (n+1)

# m 번 반복하며 graph 에 관계 추가
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

# BFS 진행
bfs(a)

# b 번 사람에 대한 촌수 값이 있는 경우
if answer[b]:
    print(answer[b])
else:
    print(-1)