## 문제 : 백준 10826번 - 피보나치 수 4
## 링크 : https://www.acmicpc.net/problem/10826


## 풀이

# n 입력
n = int(input())

d = [0] * 10001

d[0], d[1] = 0, 1

# Bottom-Up 진행
for i in range(2, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])