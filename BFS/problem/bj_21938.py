## 문제 : 백준 21938번 - 영상처리
## 링크 : https://www.acmicpc.net/problem/21938

## 풀이
### - 입력 : N(화면 세로), M(화면 가로) (1 <= N, M <= 1000) / R_(i, j), G_(i, j), B_(i, j) (0 <= RGB_(i, j) <= 255) / T(경계값) (0 <= T <= 255)
### - 출력 : 화면에 있는 물체의 개수 / 물체가 없다면 0
### - 시간 제한 : 1초 (연산 약 2천만회)
### - 메모리 제한 : 512MB (리스트 원소 약 7000만개)
### - 가능한 시간 복잡도 : ex) O(NlogN)

from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y, visited, board, N, M):
    '''
        BFS
    '''
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 255 and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return visited


def apply_with_threshold(board, T):
    '''
        Convert board to threshold_board
    '''
    convert_board = []
    for row in board:
        temp_board = []
        for i in range(len(row) // 3):
            temp_board.append(round(sum(row[i * 3:i * 3 + 3]) / 3, 1))
            temp_board = list(map(lambda x: 255 if x >= T else 0, temp_board))
        convert_board.append(temp_board)
    return convert_board


def calculate_num_of_object(board, visited, N, M):
    '''
        Calculate # of objects
    '''
    num_of_objects = 0
    for nr, row in enumerate(board):
        for nc, col in enumerate(row):
            if board[nr][nc] == 255 and visited[nr][nc] == False:
                visited = bfs(nr, nc, visited, board, N, M)
                num_of_objects += 1
    return num_of_objects
    

def solution():
    # 1) Input Values
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    T = int(input())
    
    # 2) Convert board to threshold_board
    convert_board = apply_with_threshold(board, T)

    # 3) Calculate # of objects
    num_of_objects = calculate_num_of_object(convert_board, visited, N, M)
    
    return num_of_objects
    

# Input Test
answer = solution()
print(answer)