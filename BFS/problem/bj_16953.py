## 문제 : 백준 16953번 - A -> B
## 링크 : https://www.acmicpc.net/problem/16953

## 풀이

# A, B 입력
A, B = map(int, input().split())

cnt = 1
while A != B:
    if (str(B)[-1] != '1' and B % 2 != 0) or A > B:
        cnt = -1
        break
    elif str(B)[-1] == '1':
        B = int(str(B)[:-1])
    elif B % 2 == 0:
        B = B // 2

    cnt += 1

print(cnt)