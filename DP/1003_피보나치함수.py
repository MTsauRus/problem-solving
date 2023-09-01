### 피보나치 함수 (S3)
import sys
input = sys.stdin.readline

ans = [0 for i in range(41)]
ans[0] = (1, 0)
ans[1] = (0, 1)
for i in range(2, 41):
    ans[i] = (ans[i-1][0]+ans[i-2][0], ans[i-1][1]+ans[i-2][1])
    
N = int(input())
for _ in range(N):
    next = int(input())
    print(*ans[next])