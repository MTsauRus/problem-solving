### 깊이 우선 탐색 1 (S2), 깊이 우선 탐색 2 (S2)
import sys
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
V, E, s = map(int, input().split())
G = [[] for _ in range(V+1)]

for i in range(E):
    a, b = map(int, input().split())
    heappush(G[a], -b)
    heappush(G[b], -a)
    
    
visited = [0] * (V+1)

global num
num = 2
def dfs(a):
    global num
    for i in range(len(G[a])):
        next = -heappop(G[a])
        if visited[next] == 0:
            visited[next] = num
            num += 1
            dfs(next)
            
visited[s] = 1            
dfs(s)

for i in range(1, V+1):
    print(visited[i])            
