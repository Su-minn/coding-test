## 문제 : 백준 15680번 - 연세대학교
## 링크 : https://www.acmicpc.net/problem/15680

## 풀이
### - 입력 : N (N = 0 or 1)
### - 출력 : N = 0 인 경우, 연세대학교 영문명 / N = 1 인 경우, 연세대학교 슬로건
### - 시간 제한 : 1초
### - 메모리 제한 : 128MB


def solution():
    N = input()

    if N == '0':
        print('YONSEI')
    elif N == '1':
        print('Leading the Way to the Future')

# Input Test
solution()