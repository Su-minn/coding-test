## 문제 : 백준 13301번 - 타일 장식물
## 링크 : https://www.acmicpc.net/problem/13301

## 풀이 1)

# N 입력
N = int(input())

# DP Table
d = [0] * (N + 2)

d[1], d[2] = 1, 1

# Bottom-Up 진행
for i in range(3, N+1):
    d[i] = d[i-1] + d[i-2]

# N 둘레
if N == 1:
    ans = 4
elif N == 2:
    ans = 6
else:
    ans = (d[N] + 2 * d[N-1] + d[N-2]) * 2

print(ans)


## 풀이 2)

# N 입력
N = input(input())

# DP Table
d = [0, 1] + [0 for _ in range(N)]

# i 번째 정사각형 한 변의 길이 = i-1 번째 정사각형 한 변의 길이 + i-2 번째 정사각형 한 변의 길이
for i in range(2, N+2):
    d[i] = d[i-2] + d[i-1]

# N 개 타일의 둘레 = 2 * (N 번째 정사각형 한 변의 길이 + N+1 번째 정사각형 한 변의 길이)
print(2(d[N] + d[N+1]))
