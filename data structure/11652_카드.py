import sys
from collections import Counter

N = int(input())
cntr = Counter()
lst = []
for i in range(N):
    lst.append(int(input()))
cntr.update(lst)
print(sorted(cntr.most_common(), key=lambda x:(-x[1],x[0]))[0][0])
