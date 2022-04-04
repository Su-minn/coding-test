## 문제 : 백준 16395번 - 파스칼의 삼각형
## 링크 : https://www.acmicpc.net/problem/16395


## 풀이

# n, k 입력
n, k = map(int, input().split())

# DP table 생성
d = [[0] * i for i in range(1, n+1)]

# DP table 초기화
for i, row in enumerate(d):
    l = len(row)
    d[i][0], d[i][l-1] = 1, 1

# Top-down 진행
def calculate_sum(n, k):
    if d[n-1][k-1] == 1:
        return 1

    if d[n-1][k-1] == 0: d[n-1][k-1] = calculate_sum(n-1, k-1)
    if d[n-1][k] == 0: d[n-1][k] = calculate_sum(n-1, k)

    return d[n-1][k-1] + d[n-1][k]

print(calculate_sum(n, k))