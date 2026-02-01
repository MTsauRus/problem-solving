### 깊이 우선 탐색 1 (S2), 깊이 우선 탐색 2 (S2), 깊이 우선 탐색 3 (S2)
import sys
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
V, E, s = map(int, input().split())
G = [[] for _ in range(V+1)]

for i in range(E):
    a, b = map(int, input().split())
    heappush(G[a], b)
    heappush(G[b], a)
    
    
visited = [False] * (V+1)
ans = [-1] * (V+1)

def dfs(a, depth):
    for i in range(len(G[a])):
        next = heappop(G[a])
        if not visited[next]:
            visited[next] = True
            ans[next] = depth
            dfs(next, depth+1)
            
visited[s] = True
dfs(s, 1)
ans[s] = 0

for i in range(1, V+1):
    print(ans[i])            
