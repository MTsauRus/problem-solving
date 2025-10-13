### 12865 평범한 배낭 (G5)
### dp, 배낭문제
import sys
input = sys.stdin.readline

N, W = map(int, input().split())
value, weight = [0], [0]
for _ in range(N):
    w, v = map(int, input().split())
    value.append(v)
    weight.append(w)

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
for i in range(1, N+1): 
    for w in range(1, W+1): # w: 현재 가방이 허용하는 최대 무게
        if weight[i] > w: # 현재 보석의 무게가 가방이 허용하는 무게보다 큰 경우 패스
            dp[i][w] = dp[i-1][w]
        else:
            # i번째 보석을 가방에 넣는다고 가정
            # 남은 가방의 무게는 w-weight[i]
            # i번째 보석을 포함하지 않고 w-weight[i]만큼의 무게를 허용하는 가방 value의 최대치를 더하자.
            dp[i][w] = max(dp[i-1][w], value[i] + dp[i-1][w-weight[i]]) 

print(dp[N][W])