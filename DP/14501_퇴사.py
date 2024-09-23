### 퇴사 (S3)
import sys
input = sys.stdin.readline

N = int(input())
eta = [0] * (N+1)
cost = [0] * (N+1)
ans = [0] * (N+2)
for i in range(1, N+1):
    a, b = map(int, input().split())
    eta[i] = a
    cost[i] = b

for i in range(N, 0, -1):
    if i + eta[i] <= N+1:
        ans[i] = max(ans[i+1], ans[i+eta[i]] + cost[i])
    else:
        ans[i] = ans[i+1]

print(ans[1])

sys.setRecursionlimit(10**6)