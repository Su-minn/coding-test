## 문제 : 백준 12904번 - A와 B
## 링크 : https://www.acmicpc.net/problem/12904

## 풀이

S = input()
T = input()

s_len = len(S)
t_len = len(T)
i = 0

# T 와 S 의 길이 차만큼 실행 (연산 횟수와 동일)
# T 를 S 로 만드는 역연산 진행
for _ in range(t_len - s_len):
    # T 의 맨 뒤가 B면 B를 제거하고, 문자열 뒤집기
    if T[-1] == 'B':
        T = T[:-1]
        T = T[::-1]
    # T 의 맨 뒤에 A 면, A 를 제거
    else:
        T = T[:-1]

if S == T:
    print(1)
else:
    print(0)

