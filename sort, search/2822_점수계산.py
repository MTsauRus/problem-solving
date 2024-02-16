### 점수 계산 (S5)
import sys
input = sys.stdin.readline

l = []
ans=0
for i in range(1, 9):
    a=int(input())
    l.append([a,i])
l.sort(reverse=True)
l=l[0:5]
ans=0
k=[]
for tmp in l:
    ans += tmp[0]
    k.append(tmp[1])
k.sort()
print(ans)
print(*k)
