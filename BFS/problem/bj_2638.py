## 문제 : 백준 2638번 - 치즈
## 링크 : https://www.acmicpc.net/problem/2638

## 풀이
### - 입력 : 모눈종이 크기 N, M (5 <= N, M <= 100) / A_(r, c) = {1, 0} (치즈가 있는 부분 1, 없으면 0)
### - 출력 : 치즈가 모두 녹아없어지는데 걸리는 시간
### - 시간 제한 : 1초
### - 메모리 제한 : 128MB
### - Key Points
###   : 1) 모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정 -> 치즈 외부 공기 파트는 하나로 연결 -> BFS 탐색
###   : 2) 4변 중 적어도 2변 이상이 접촉한 부분만 녹음 -> BFS 과정에서 2번 이상 count된 경우에만 녹음


from collections import deque
import copy
import queue
import sys
input = sys.stdin.readline


def bfs(board, N, M):
    """
        BFS
    """
    exist_cheese = False
    visited = [[False] * M for _ in range(N)]
    queue = deque([(0, 0)])
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and visited[nx][ny] == False:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                elif board[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    exist_cheese = True
                elif board[nx][ny] == 1 and visited[nx][ny] == True:
                    board[nx][ny] = 0
    return board, exist_cheese


def solution():
    # 1) Input Values
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    t = 0
    
    # 2) Check outer area
    exist_cheese = True
    while exist_cheese:
        temp_board = copy.deepcopy(board)
        board, exist_cheese = bfs(temp_board, N, M)
        t += 1
    return t - 1

# Input Test
answer = solution()
print(answer)