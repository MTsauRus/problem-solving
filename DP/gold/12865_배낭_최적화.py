### 12865 평범한 배낭 (G5)
### dp, 배낭문제
### 1차원 배열로 최적화
import sys
input = sys.stdin.readline

N, W = map(int, input().split())
value, weight = [0], [0]
for _ in range(N):
    w, v = map(int, input().split())
    value.append(v)
    weight.append(w)

dp = [0 for i in range(W+1)] # 1차원 배열로 변경 -> 최대 허용 무게만을 인덱스로 사용
for i in range(1, N+1): 
    for w in range(W, weight[i]-1, -1): # W부터 현재 무게까지 역순으로 순회
        ## 항상 가방보다 큰 보석만을 순회하므로 아래 코드는 필요 없음
        #if weight[i] > w: 
        #    dp[i][w] = dp[i-1][w]
        
        # 우변에 있는 dp[w]가 이전 순회의 dp[i][w]이므로 현재 순회에서 dp[i-1][w]와 동일함
        dp[w] = max(dp[w], value[i] + dp[w-weight[i]]) 

print(dp[W])