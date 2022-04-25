## 문제 : 백준 1706번 - 크로스워드
## 링크 : https://www.acmicpc.net/problem/1706

## 풀이
import sys

# R, C 입력
R, C = map(int, input().split())

# board 생성
board = []

# 퍼즐 입력
for _ in range(R):
    board.append(sys.stdin.readline().strip())

# 전치된 board 생성
tr_board = [''.join(x) for x in zip(*board)]

# board 와 전치 board 를 연결한 list 생성
sum_board = board + tr_board

# 금지칸 (#) 을 기준으로 분리
temp = [row.split('#') for row in sum_board]

# 단어인 경우만 (길이가 2이상) 리스트 원소로 삽입
filtered_board = [x for row in temp for x in row if len(x) >= 2]

# 사전순 정렬
filtered_board.sort()

# 첫번째 낱말 출력
print(filtered_board[0])
