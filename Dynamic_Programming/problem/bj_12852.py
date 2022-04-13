## 문제 : 백준 12852번 - 1로 만들기 2
## 링크 : https://www.acmicpc.net/problem/12852

## 풀이 1)

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

## 풀이 2)

# N 입력
N = int(input())

# DP Table
d = [[], [1], [2, 1], [3, 1]] + [[] for _ in range(4, N+1)]

for i in range(4, N+1):
    if i % 6 == 0:
        num_list = [d[i-1], d[i//2], d[i//3]]
    elif i % 3 == 0:
        num_list = [d[i-1], d[i//3]]
    elif i % 2 == 0:
        num_list = [d[i-1], d[i//2]]
    else:
        num_list = [d[i-1]]

    # d[i] 는 num_list 중 가장 최소의 길이를 갖는 리스트에 [i] 를 더한 것
    d[i] = [i] + min(num_list, key=lambda x: len(x))

# 출력
print(len(d[N]) - 1)
for x in d[N]:
    print(x, end=' ')
