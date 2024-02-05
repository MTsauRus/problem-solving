### 붙임성 좋은 총총이 (S4)
import sys
input = sys.stdin.readline

S = set()
n = int(input())

while n > 0:
    n -= 1
    tmp = list(map(lambda x : x.strip(), input().split()))
    if "ChongChong" in tmp:
        S.add(tmp[0])
        S.add(tmp[1])
        break
while n > 0:
    n -= 1
    tmp = list(map(lambda x : x.strip(), input().split()))
    if tmp[0] in S or tmp[1] in S:
        S.add(tmp[0])
        S.add(tmp[1])

print(len(S))
        