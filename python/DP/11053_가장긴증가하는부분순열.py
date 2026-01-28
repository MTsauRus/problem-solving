### 가장 긴 증가하는 부분 수열(S2)
### DP
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

cur_max = nums[0]
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    now = nums[i]
    dp_max = 0
    for j in range(0, i):
        if now > nums[j] and dp[j] > dp_max: 
            dp_max = dp[j] 
    dp[i] = dp_max + 1
    
print(max(dp))
