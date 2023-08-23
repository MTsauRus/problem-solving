### 통계학 (S3)
import sys
input = sys.stdin.readline
from collections import Counter
import math

N = int(input())
num = []
for n in range(N):
    num.append(int(input()))

num.sort()
avg = round(sum(num)/N)
mid = num[N//2]
tmp = Counter(num)
tmp2=sorted(list(tmp.items()),key=lambda x:-x[1])
if len(tmp2) == 1:
    usually = tmp2[0][0]
elif tmp2[0][1] == tmp2[1][1]:
    usually = tmp2[1][0]
else:
    usually = tmp2[0][0]
length = abs(max(num)-min(num))
print(avg)
print(mid)
print(usually)
print(length)
