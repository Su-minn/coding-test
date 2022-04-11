## 문제 : 백준 12852번 - 1로 만들기 2
## 링크 : https://www.acmicpc.net/problem/12852

## 풀이

# N 입력
N = int(input())

# DP Table
d = [0] * (10**6 + 1)

# DP Bottom-Up
for i in range(2, N + 1):
    # 1을 빼는 경우
    d[i] = d[i - 1] + 1

    # 3 으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 2 로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

# 연산 횟수 출력
print(d[N])
# 연산 과정 출력
while N != 0:
    # 연산 과정 출력
    print(N, end=' ')

    temp = N - 1

    # 3 으로 나누어 떨어지는 경우
    if N % 3 == 0:
        temp = temp if d[N - 1] <= d[N // 3] else N // 3
    # 2 로 나누어 떨어지는 경우
    if N % 2 == 0:
        temp = temp if d[temp] <= d[N // 2] else N // 2

    N = temp
