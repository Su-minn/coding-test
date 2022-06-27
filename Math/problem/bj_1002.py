## 문제 : 백준 1002번 - 터렛
## 링크 : https://www.acmicpc.net/problem/1002

## 풀이
### - 입력 : T (테스트 케이스 개수) / x1, y1, r1, x2, y2, r2 (-10,000 <= x1, y1, x2, y2 <= 10,000), (1 <= r1, r2 <= 10,000)
### - 출력 : 두 원의 겹치는 교점의 수, 무한대인 경우 -1
### - 시간 제한 : 2초
### - 메모리 제한 : 128MB
### - Key Points
###   : 1) 중심 (x1, y1), 반지름 r1인 원과, 중심 (x2, y2), 반지름 r2인 원의 교점 갯수 -> 두 원의 위치 관계

from math import sqrt
import sys
input = sys.stdin.readline


def solution():
    T = int(input())

    # Test Case
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        d = sqrt((x1 - x2)**2 + (y1 - y2)**2)
        if d > r1 + r2 or d < abs(r1 - r2):
            intersection_point = 0
        # circumscription(외접) or inscription(내접) or 일치
        elif d == r1 + r2 or d == abs(r1 - r2):
            if d == 0:
                intersection_point = -1
            else:
                intersection_point = 1
        elif d < r1 + r2:
            intersection_point = 2
        print(intersection_point)


# Input Test
solution()