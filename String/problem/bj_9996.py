## 문제 : 백준 9996번 - 한국이 그리울 땐 서버에 접속하지
## 링크 : https://www.acmicpc.net/problem/9996

## 풀이

import sys

# 파일의 개수 N 개 입력
N = int(input())

# 패턴 입력 / '*' 기준 왼쪽, 오른쪽으로 구분
left, right = sys.stdin.readline().split('*')

# N 개의 파일 읽고 결과 출력
for i in range(N):
    file = sys.stdin.readline()

    # 왼쪽부터 left 길이만큼 file 문자열과 같고, 오른쪽에서 right 길이만큼 file 문자열과 같으면 'DA' 출력
    # file 의 길이가 pattern 의 길이 합보다 큰 경우에만 'DA' 출력
    if left == file[:len(left)] and right == file[-len(right):] and len(file) >= len(left) + len(right):
        print('DA')
    # 아니면 'NE' 출력
    else:
        print('NE')
