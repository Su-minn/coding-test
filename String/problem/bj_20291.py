# 문제 : 백준 20291번 - 파일 정리
# 링크 : https://www.acmicpc.net/problem/20291

# 풀이
import sys
from collections import defaultdict

# 파일의 갯수 N 입력
N = int(input())

# defaultdict 로 확장자 사전 생성
extension_dict = defaultdict(int)

# N 번 반복
for _ in range(N):
    # '.' 을 기준으로 확장자 parsing
    _, extension = sys.stdin.readline().split('.')
    # defaultdict 내에 key 값이 없는 경우 (새로운 확장자) 값 1 (default 값 0)
    # defaultdict 내에 key 값이 있는 경우 (존재하는 확장자) 기존 값 +1
    extension_dict[extension.strip()] += 1

# 사전순으로 정렬
# output type 은 list, 원소는 tuple 로 구성
sorted_extension = sorted(extension_dict.items())

# 알맞은 형식으로 출력
for el in sorted_extension:
    k, v = el
    print(k, v)