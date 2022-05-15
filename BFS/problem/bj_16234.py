import sys
from collections import deque

# bfs 함수 정의
def bfs(x, y):
    # queue 에 시작 좌표 삽입
    queue = deque([(x, y)])
    # 해당 좌표 방문 처리
    visited[x][y] = True
    # 연합 인구 수 리스트 생성
    union = [board[x][y]]

    # queue 에 값이 없을 때 까지 반복
    while queue:
        x, y = queue.popleft()
        # 상, 하, 좌, 우 좌표 확인
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            # (1) 탐색 좌표 nx, ny 가 유효하지 않거나, (2) 이미 방문한 좌표인 경우 pass
            if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny] == True:
                continue
            # 문제의 조건에 맞는 경우 (L <= 인구 차 <= R) 연합 설정
            if L <= abs(board[x][y] - board[nx][ny]) <= R:
                # queue 에 해당 좌표 삽입
                queue.append((nx, ny))
                # 해당 좌표 방문 처리
                visited[nx][ny] = True
                # 연합 인구 수 리스트에 등록
                union.append(board[nx][ny])

    # 연합이 존재하는 경우, 연합 국가간 인구 인동 진행
    if len(union) >= 2:
        updated_num = sum(union) // len(union)
        for x in range(N):
            for y in range(N):
                if visited[x][y] == True:
                    board[x][y] = updated_num
        # 인구 이동이 일어났으므로, True 반환
        return True
    # 인구 이동이 일어나지 않았으므로, False 반환
    return False

# N, L, R 입력
N, L, R = map(int, input().split())
# N x N 인구수 입력
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 인구 이동 일 수
move_day = 0
# 더 이상 인구 이동이 일어나지 않을 때까지, 모든 좌표에 있어서 bfs 탐색 진행
move = True

while move:
    move = False
    # 방문 여부 초기화 진행
    visited = [[False] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            # 해당 좌표를 방문하지 않은 경우, bfs 로 탐색 진행
            if visited[x][y] == False:
                temp = bfs(x, y)
                # bfs 결과가 True 인 경우에만 move 를 True 로 변경
                if temp:
                    move = temp
    # move 가 True 인 경우 (인구 이동이 일어난 경우), 일자 추가
    if move:
        move_day += 1

print(move_day)

# 반례
# https://www.acmicpc.net/board/view/53872