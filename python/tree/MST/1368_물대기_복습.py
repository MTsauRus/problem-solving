import sys
input = sys.stdin.readline

N = int(input())
first = [0]
for _ in range(N):
    first.append(int(input()))

G = [[] for _ in range(N+1)]
G[0] = first

for i in range(1, N+1):
    top = first[i]
    G[i] = [top] + list(map(int, input().split()))
    
dist = [float('inf')] * (N+1)
dist[0] = 0
visited = [False] * (N+1)

ans = 0

for _ in range(N+1):
    now = -1
    localSum = float('inf')
    
    for i in range(N+1):
        if not visited[i] and dist[i] < localSum:
            localSum = dist[i]
            now = i
        
    visited[now] = True
    ans += dist[now]
    
    for i in range(N+1):
        if not visited[i]:
            if dist[i] > G[now][i]:
                dist[i] = G[now][i]

print(ans)
        
