### 너비 우선 탐색 1, 너비 우선 탐색 2(S2)
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
from collections import deque

V, E, s = map(int, input().split())
G = [[] for _ in range(V+1)]
for i in range(E):
    a, b = map(int, input().split())
    heappush(G[a], -b)
    heappush(G[b], -a)
 
visited = [0] * (V+1)   
global cnt
cnt = 1

def bfs(v):
    global cnt    
    queue = deque()
    visited[v] = cnt
    cnt += 1
    queue.append(v)
    while queue:
        now = queue.popleft()
        for i in range(len(G[now])):
            next = -heappop(G[now])
            if visited[next] == 0:
                visited[next] = cnt
                cnt += 1
                queue.append(next)

bfs(s)
for i in range(1, V+1):
    print(visited[i])