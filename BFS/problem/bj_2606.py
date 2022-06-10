## 문제 : 백준 2606번 - Problem Title
## 링크 : https://www.acmicpc.net/problem/2606

## 풀이
### - 입력 : N (컴퓨터의 수), 1 <= N <= 100, M (연결된 컴퓨터 쌍의 수), M개의 번호 쌍
### - 출력 : 1번 컴퓨터를 통해 바이러스에 걸리게되는 컴퓨터의 수
### - 시간 제한 : 1초
### - 메모리 제한 : 128MB

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    num = 0
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for next in graph[v]:
            if visited[next] == False:
                queue.append(next)
                visited[next] = True
                num += 1
    return num
    

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    left, right = map(int, input().split())
    graph[left].append(right)
    graph[right].append(left)

num = bfs(1)

print(num)