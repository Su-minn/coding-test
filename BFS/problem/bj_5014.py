## 문제 : 백준 5014번 - 스타트링크
## 링크 : https://www.acmicpc.net/problem/5014

## 풀이
### - 입력 : F(총 층 수), S(현재 층), G(목표 층) (1 <= S, G <= F <= 1,000,000) // U(위 이동 층 수), D(아래 이동 층 수) (0 <= U, D <= 1,000,000)
### - 출력 : S층에서 G층으로 가기 위해 눌러야하는 버튼 수 최솟값 or "use the stairs" (이동 불가능한 경우)
### - 시간 제한 : 1초 -> 약 2,000만 번 연산 가능
### - 메모리 제한 : 256MB -> int 자료형 List 원소 갯수 약 2,000 만 개 사용 가능

from collections import deque

## Sol 1) visited List & time 각각 저장

# BFS
def bfs(S):
    # Append current floor and time [floor, time]
    queue = deque([[S, 0]])
    visited[S] = True
    
    while queue:
        v, t = queue.popleft()
        
        # Arrived at G floor
        if v == G:
            return t
        
        for new_s in (v + U, v - D):
            if 1<= new_s <= F and visited[new_s] == False:
                queue.append([new_s, t+1])
                visited[new_s] = True
    return -1

def solution():
    result = bfs(S)
    answer = "use the stairs" if result == -1 else result
    return answer

F, S, G, U, D = map(int, input().split())
visited = [False] * (F + 1)
ans = solution()
print(ans)


## Sol 2) visited List에 time 저장

# BFS
def bfs(S):
    # Append current floor and time [floor, time]
    queue = deque([S])
    visited[S] = 0
    
    while queue:
        v = queue.popleft()
        
        # Arrived at G floor
        if v == G:
            return visited[v]
        
        for new_s in (v + U, v - D):
            if 1<= new_s <= F and visited[new_s] == -1:
                queue.append(new_s)
                visited[new_s] = visited[v] + 1
    return -1

def solution():
    result = bfs(S)
    answer = "use the stairs" if result == -1 else result
    return answer

F, S, G, U, D = map(int, input().split())
visited = [-1] * (F + 1)
ans = solution()
print(ans)