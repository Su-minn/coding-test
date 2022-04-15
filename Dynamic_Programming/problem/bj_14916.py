## 문제 : 백준 14916번 - 거스름돈
## 링크 : https://www.acmicpc.net/problem/14916

## 풀이 1)

# n 입력
n = int(input())

money_list = [2, 5]

# DP Table
# 최대 n 인 100000 // 최소 거스름 돈 2원 = 50000 이기에, 50001은 INF
d = [50001] * (100000 + 1)

d[0] = 0
# Bottom-Up 진행
for money in money_list:
    for i in range(money, n+1):
        # money 원을 추가해 만들 수 있는 경우
        if d[i - money] != 50001:
            d[i] = min(d[i], d[i - money] + 1)

# 만들 수 없는 경우
if d[n] == 50001:
    print(-1)
else:
    print(d[n])

## 풀이 2)
n = int(input())

# DP Table
d = [0, 0, 1, 0, 2, 1] + [0 for _ in range(n)]

# Bottom-Up 진행
for i in range(6, n+1):
    if i % 5 == 0:
        d[i] = d[i-5] + 1
    else:
        d[i] = d[i-2] + 1

if d[n] == 0:
    print(-1)
else:
    print(d[n])