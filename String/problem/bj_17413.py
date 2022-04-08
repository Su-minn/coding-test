## 문제 : 백준 17413번 - 단어 뒤집기 2
## 링크 : https://www.acmicpc.net/problem/17413

## 풀이

# 문자열 s 입력
s = input()

tag = False
word = ""

for i in s:
  if i == '<':
    tag = True

  if i == '>':
    print(i, end='')
    tag = False

  if tag == True or i == ' ':
    if word:
      print(word[::-1], end='')
      word = ""
    print(i, end='')
  elif i != '>':
    word += i
print(word[::-1])