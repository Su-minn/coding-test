from jussuit_notes_ps.utils import *

## 문제 : 백준 1075번 - 나누기
## 링크 : https://www.acmicpc.net/problem/1075

## 풀이
### - 입력 : N(100 =< N =< 2,000,000,000, 정수), F(F <= 100, 정수)
### - 출력 : F 로 나누어 떨어지는 N 의 가장 작은 맨 뒤 두자리
### - 시간 제한 : 2초
### - 메모리 제한 : 128 MB

@time_check
def solution(*args, **kwargs):
    # N 의 뒷 두자리 버리기
    N = (int(input()) // 100) * 100
    F = int(input())

    # N 부터 N + 99 까지 반복
    for n in range(N, N+100):
        # n(N+i) 이 F 로 나누어 떨어지는 경우
        if n % F == 0:
            answer = n % 100
            answer = '0' + str(answer) if answer < 10 else answer
            break

    return answer

# Input Test
answer = solution()
print(answer)
