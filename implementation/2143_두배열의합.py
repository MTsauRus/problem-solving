### 2143. 두 배열의 합 (G3)
### 누적 합, 정렬, 이분 탐색
import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

key = int(input())
n = int(input())
num1 = list(map(int, input().split()))
snum1 = num1[:]
for i in range(1, n):
    snum1[i] = snum1[i-1] + snum1[i]
m = int(input())
num2 = list(map(int, input().split()))
snum2 = num2[:]
for i in range(1, m):
    snum2[i] = snum2[i-1] + snum2[i]

for i in range(n):
    for j in range(i+1, n):
        snum1.append(snum1[j] - snum1[i])
        
        
for i in range(m):
    for j in range(i+1, m):
        snum2.append(snum2[j] - snum2[i])

snum1.sort()
snum2.sort()

ans = 0

for i in range(len(snum1)):
    now = snum1[i]
    left = bisect_left(snum2, key-now)
    right = bisect_right(snum2, key-now)
    ans += right-left
print(ans)