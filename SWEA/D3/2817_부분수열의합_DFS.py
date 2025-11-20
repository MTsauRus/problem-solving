### 2817. 부분 수열의 합
### 완전 탐색, dfs, S2?

T = int(input())

def dfs(idx, res):
    global ans
    
    if res == K:
        ans += 1
        return
    
    elif res > K:
        return
    
    if idx == N:
        return
    
    dfs(idx+1, res)
    dfs(idx+1, res+nums[idx])
    
for t in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    ans = 0
    dfs(0, 0)
    print(f'#{t} {ans}')