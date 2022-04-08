## 문제 : 백준 9625번 - BABBA
## 링크 : https://www.acmicpc.net/problem/9625


## 풀이


# K 입력
K = int(input())

d_a = [0] * (K + 1)
d_b = [0] * (K + 1)

# 첫번째 항 설정
d_a[1] = 0
d_b[1] = 1

# Bottom-Up 진행
for i in range(1, K):
    d_a[i+1] = d_b[i]
    d_b[i+1] = d_a[i] + d_b[i]

print(d_a[K], d_b[K])