## 문제 : 백준 1388번 - 바닥 장식
## 링크 : https://www.acmicpc.net/problem/1388

## 풀이
### - 입력 : N(세로 크기), M(가로 크기) (1 <= N, M <= 50) / A_(r, c) = {'-' or '|'}
### - 출력 : 나무 판자의 갯수
### - 시간 제한 : 2초
### - 메모리 제한 : 128MB

import sys
input = sys.stdin.readline


def get_connected_board(board, board_type, another_board_type):
    """
        연결되어있는 판자 갯수 반환
    """
    board_num = 0
    for nr, row in enumerate(board):
        for nc, c in enumerate(row):
            if nc == 0 and c == board_type:
                board_num += 1
            elif nc != 0 and board[nr][nc-1] == another_board_type and board[nr][nc] == board_type:
                board_num += 1
    return board_num


def solution():
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    reverse_board = [i for i in zip(*board)]
    row_board_num = get_connected_board(board, '-', '|')
    col_board_num = get_connected_board(reverse_board, '|', '-')
    return row_board_num + col_board_num


# Input Test
answer = solution()
print(answer)