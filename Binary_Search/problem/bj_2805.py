from jussuit_notes_ps.utils import *

## 문제 : 백준 2805번 - 나무 자르기
## 링크 : https://www.acmicpc.net/problem/2805

## 풀이
### - 입력 : N (나무의 수) (1 <= N <= 1,000,000) // M (가져가야하는 나무의 길이) (1 <= M <= 2,000,000,000) // 나무의 높이 (나무 높이의 합 >= M)
### - 출력 : 적어도 M 미터 나무를 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값
### - 시간 제한 : 1초
### - 메모리 제한 : 256MB
### - 가능한 시간 복잡도 : Nlog(M)

# Sol 1) Binary Search
@time_check
def solution1(*args, **kwargs):
    import sys
    input = sys.stdin.readline
    import random

    # 1) Input values
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    min_H, max_H = 0, max(trees)

    # 2) Binary Search
    while True:
        sum_h = 0
        if min_H == max_H:
            return min_H

        H = max_H if min_H + 1 == max_H else (min_H + max_H) // 2
        for tree in trees:
            cut_h = 0 if tree - H < 0 else tree - H
            sum_h += cut_h
        if sum_h >= M: min_H = H
        else: max_H = H - 1

# Input Test
H = solution1()
print(H)


# Sol 2) Random Binary Search
@time_check
def solution2(*args, **kwargs):
    import sys
    input = sys.stdin.readline
    import random

    # 1) Input values
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    min_H, max_H = 0, max(trees)
    H = (min_H + max_H) // 2

    # 2) Random Binary Search
    while True:
        sum_h = 0
        if min_H == max_H:
            return H

        for tree in trees:
            cut_h = 0 if tree - H < 0 else tree - H
            sum_h += cut_h
        if sum_h >= M: min_H = H
        else: max_H = H - 1

        H = random.randint(min_H, max_H)

# Input Test
H = solution2()
print(H)