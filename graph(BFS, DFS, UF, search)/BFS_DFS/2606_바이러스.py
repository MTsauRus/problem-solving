### 바이러스 (S3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V = int(input())
E = int(input())
G = [[] for _ in range(V+1)]
visited = [False] * (V+1)
for _ in range(E):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
global cnt    
cnt=0
def dfs(v):
    global cnt
    visited[v] = True
    for next in G[v]:
        if not visited[next]:
            cnt += 1
            dfs(next)
    
dfs(1)
print(cnt)
        
    