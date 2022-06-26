## 문제 : 백준 1929번 - 소수 구하기
## 링크 : https://www.acmicpc.net/problem/1929

## 풀이
### - 입력 : M, N (M 이상 N 이하의 소수) (1 <= M <= N <= 1,000,000)
### - 출력 : 한 줄에 하나씩, 증가하는 순서대로 M 이상 N 이하의 모든 소수 출력
### - 시간 제한 : 2초
### - 메모리 제한 : 256MB
### - 가능한 시간 복잡도 : O(NlogN)
### - Key Points
###   : 1) 소수 check 시, 제곱근까지만 나누어지는 지를 확인


from math import sqrt

def check_prime_number(num):
    if num == 1:
        return False

    for q in range(2, int(sqrt(num)) + 1):
        if num % q == 0:
            return False
    return True


def solution():
    M, N = map(int, input().split())

    for num in range(M, N + 1):
        if check_prime_number(num):
            print(num)


# Input Test
solution()