N, K = map(int, input().split())
num = list(map(int, input().split()))

ans = float('inf')

def dfs(depth, tmp_sum):
    global ans
    if (depth == N):
        ans = min(abs(tmp_sum - K), ans)
        return

    dfs(depth+1, tmp_sum + num[depth])
    dfs(depth+1, tmp_sum - num[depth])
    dfs(depth+1, tmp_sum * num[depth])

dfs(1, num[0])
print(ans)