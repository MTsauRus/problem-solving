### 국영수 (S4)
import sys
input = sys.stdin.readline
N=int(input())
l=[]
for i in range(N):
    name, kor, eng, math = input().split()
    l.append([int(kor), int(eng), int(math), name])

l.sort(key=lambda x : (-x[0], x[1], -x[2], x[3]))
for a in l:
    print(a[3])