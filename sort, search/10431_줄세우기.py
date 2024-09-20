### 줄세우기 (S5)
### 정렬, 구현
import sys
input = sys.stdin.readline

a=int(input())
for i in range(a):
    ans = 0
    l = list(map(int,input().split()))
    l.pop(0)
    for j in range(20):
        for k in range(0, j):
            if l[k] > l[j]:
                l[k], l[j] = l[j], l[k]
                ans += 1
    print(i+1, ans)