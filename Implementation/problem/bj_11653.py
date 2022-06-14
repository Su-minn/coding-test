## 문제 : 백준 11653번 - 소인수분해
## 링크 : https://www.acmicpc.net/problem/11653

## 풀이
### - 입력 : N (1 <= N <= 10,000,000)
### - 출력 : N의 소인수분해 결과를 한 줄에 하나씩 오름차순 출력 / N이 1인 경우 출력 X
### - 시간 제한 : 1초
### - 메모리 제한 : 256 MB

def divide_by_prime(N):
    if N == 1:
        return
    for i in range(2, N+1):
        if N % i == 0:
            print(i)
            N //= i
            break
    divide_by_prime(N)


def solution():

    # Input N
    N = int(input())
    divide_by_prime(N)

solution()