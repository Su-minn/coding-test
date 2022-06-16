## 문제 : 백준 5014번 - 스타트링크
## 링크 : https://www.acmicpc.net/problem/5014

## 풀이
### - 입력 : F(총 층 수), S(현재 층), G(목표 층) (1 <= S, G <= F <= 1000000) // U(위 이동 층 수), D(아래 이동 층 수) (0 <= U, D <= 1000000)
### - 출력 : S층에서 G층으로 가기 위해 눌러야하는 버튼 수 최솟값 or "use the stairs" (이동 불가능한 경우)
### - 시간 제한 : 1초
### - 메모리 제한 : 256MB



def solution(F, S, G, U, D):

    answer = True
    return answer

F, S, G, U, D = map(int, input().split())
ans = solution(F, S, G, U, D)
print(ans)