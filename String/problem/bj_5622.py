from jussuit_notes_ps.utils import *

## 문제 : 백준 5622번 - 다이얼
## 링크 : https://www.acmicpc.net/problem/5622

## 풀이
### - 입력 : 대문자 word (2 <= len(word) <= 15)
### - 출력 : 다이얼을 걸기 위한 최소 시간
### - 시간 제한 : 1초
### - 메모리 제한 : 128MB

@time_check
def solution():
    word = input()
    t = 0
    for c in word:
        if 'A' <= c <= 'R': t += ((ord(c) - 2) // 3) - 18
        elif 'R' < c < 'Z': t += ((ord(c) - 3) // 3) - 18
        elif c == 'Z': t += 10
        else: t += 0

    return t

# Input Test
t = solution()
print(t)
