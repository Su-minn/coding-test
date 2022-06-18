## 문제 : 백준 13549번 - 숨바꼭질 3
## 링크 : https://www.acmicpc.net/problem/13549

## 풀이
### - 입력 : N(수빈 위치), K(동생 위치) (0 <= N, K <= 100,000)
### - 출력 : t (수빈이가 동생을 찾는 가장 빠른 시간)
### - 시간 제한 : 2초
### - 메모리 제한 : 512MB

from collections import deque

# BFS
def bfs(N, K, visited):
    queue = deque([N])
    visited[N] = 0
    
    while queue:
        v = queue.popleft()
        
        for idx, new in enumerate((v+1, v-1, v*2)):
            if 0 <= new <= 100000:
                if 0 <= idx <= 1:
                    if visited[new] == -1 or (visited[v] + 1 < visited[new]):
                        visited[new] = visited[v] + 1
                        queue.append(new)
                else:
                    if visited[new] == -1 or (visited[v] < visited[new]):
                        visited[new] = visited[v]
                        queue.append(new)
    return visited[K]


def solution():
    N, K = map(int, input().split())
    visited = [-1] * 100001
    t = bfs(N, K, visited)

    return t

# Input Test
answer = solution()
print(answer)