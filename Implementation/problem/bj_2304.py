from jussuit_notes_ps.utils import *

## 문제 : 백준 2304번 - 창고 다각형
## 링크 : https://www.acmicpc.net/problem/2304

## 풀이
### - 입력 : 기둥의 갯수(N) (1 =< N =< 1000) / 기둥 왼쪽면의 위치(L), 기둥의 높이(H) (1 =< L, H <= 1000)
### - 출력 : 창고 다각형의 면적 (정수)
### - 시간 제한 : 2초
### - 메모리 제한 : 128 MB
### - 가능한 시간 복잡도 : ~ O(N^2)

@time_check
def solution():
    import sys

    N = int(input())
    area = 0
    pre_L, pre_H = 0, 0

    # 지붕 입력 및 정렬
    roof = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    roof.sort()
    # 앞쪽으로부터 최대 높이 기둥 위치 / 높이, 뒷쪽으로부터 최대 높이 기둥 위치 / 높이 저장
    max_left_L, max_left_H = max(roof, key=lambda x: x[1])
    max_right_L, max_right_H = max(roof[::-1], key=lambda x: x[1])

    # 앞에서부터 최대 높이 기둥 위치까지 탐색하며 면적 더하기
    for L, H in roof:
        if pre_H < H:
            area += (H + pre_H * (L - pre_L - 1))
            pre_L, pre_H = L, H
        if L == max_left_L:
            break

    # 뒤에서부터 최대 높이 기둥 위치까지 탐색하며 면적 더하기
    pre_L, pre_H = 0, 0
    for L, H in roof[::-1]:
        if pre_H < H:
            area += (H + pre_H * (pre_L - L - 1))
            pre_L, pre_H = L, H
        if L == max_right_L:
            break

    # 최대 높이를 갖는 기둥이 한 개인 경우, 중복 연산된 면적 제외
    if max_left_L == max_right_L:
        area -= max_right_H
    # 최대 높이를 갖는 기둥이 여러 개인 경우, 중간 누락된 면적 추가
    else:
        area += ((max_right_L - max_left_L - 1) * max_left_H)

    return area

# Input Test
print(solution())