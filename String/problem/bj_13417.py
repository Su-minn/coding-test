# 문제 : 백준 13417번 - 카드 문자열
# 링크 : https://www.acmicpc.net/problem/13417

# 풀이

import sys
from collections import deque

T = int(input())
ans = deque([])

for _ in range(T):
    N = int(sys.stdin.readline())
    cards = sys.stdin.readline().split()
    for card in cards:
        # ans 가 비어있거나, 첫번째 카드보다 사전 순서가 뒤인 경우 뒤에 추가 (append)
        if not ans or ans[0] < card:
            ans.append(card)
        # 첫번째 카드보다 사전 순서가 앞이거나 같은 경우 앞에 추가 (appendleft)
        elif ans[0] >= card:
            ans.appendleft(card)

    # 연결하여 출력
    print("".join(ans))
    # ans 비워주기
    ans = deque([])