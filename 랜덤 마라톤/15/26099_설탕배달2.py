### 랜덤 마라톤 15
### 설탕 배달 2 (S4)
### 그리디
import sys
input = sys.stdin.readline

N = int(input())

ans = sys.maxsize

for x in range(5):
    if (N - 3*x) % 5 == 0 and N >= 3*x:
        y = (N - 3*x) // 5
        if ans > x+y:
            ans = x+y

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)