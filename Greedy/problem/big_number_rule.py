def solution():
    N, M, K = map(int, input().split())
    numbers = sorted(list(map(int, input().split())), reverse=True)

    q, r = divmod(M, K + 1)

    return numbers[0] * (K * q + r) + numbers[1] * q


ans = solution()
print(ans)
