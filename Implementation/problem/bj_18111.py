# 문제 : 백준 18111번 - 마인크래프트
# 링크 : https://www.acmicpc.net/problem/18111

# 풀이
from time import time
import sys

# N, M, B 입력
N, M, B = map(int, input().split())

# 시간 측정 시작
start_time = time()

# 땅 (board) 입력
board = []

for _ in range(N):
    board += list(map(int, sys.stdin.readline().split()))

board.sort(reverse=True)
min_h, max_h = min(board), max(board)
result = []

for h in range(min_h, max_h + 1):
    # 시간, 인벤토리
    t, inv, all = 0, B, True

    for block in board:
        h_diff = abs(block - h)

        if block > h:
            t += 2 * h_diff
            inv += h_diff
        else:
            t +=  h_diff
            inv -= h_diff
            # inventory 가 부족한 경우
            if inv < 0:
                all = False
                break

    if all == True:
        result.append([t,h])

result.sort(key = lambda x : (x[0], -x[1]))

# 시간, 땅 높이 출력
print(*result[0])

# 시간 측정 종료
end_time = time()
# 걸린 시간 출력
print(f"===== Time : {end_time - start_time:.4f} second 걸렸습니다! =====")
