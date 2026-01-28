### 1106 호텔 (G3)
### DP, 배낭 문제
import sys
input = sys.stdin.readline

C, N = map(int, input().split())
costs, values = [0], [0]
for _ in range(N):
    c, v = map(int, input().split())
    costs.append(c)
    values.append(v)

# dp[c]: 최대 c의 cost를 사용하여 얻는 최대 value
dp = [0 for i in range(100*1000+1)]
for i in range(1, N+1):
    now_cost, now_value = costs[i], values[i]
    for c in range(1, len(dp)):
        if now_cost > c:
            continue
        dp[c] = max(dp[c], now_value + dp[c-now_cost])
    
for i in range(len(dp)):
    if dp[i] >= C:
        print(i)
        break