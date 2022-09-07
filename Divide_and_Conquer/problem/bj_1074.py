## 문제 : 백준 1074번 - z
## 링크 : https://www.acmicpc.net/problem/1074


def z(N, r, c):
    if N == 0:
        return 0

    half = 1 << (N - 1)
    if r < half and c < half:
        return z(N - 1, r, c)
    elif r < half and c >= half:
        return half**2 + z(N - 1, r, c - half)
    elif r >= half and c < half:
        return half**2 * 2 + z(N - 1, r - half, c)
    elif r >= half and c >= half:
        return half**2 * 3 + z(N - 1, r - half, c - half)


N, r, c = map(int, input().split())
ans = z(N, r, c)
print(ans)
