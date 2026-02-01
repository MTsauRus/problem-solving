### 좌표 압축 (S2)
### 정렬

import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
setx = sorted(list(set(x)))
dict = {}
for i in range(len(setx)):
    dict.update({setx[i]: i})

for i in x:
    print(dict[i], end=' ')