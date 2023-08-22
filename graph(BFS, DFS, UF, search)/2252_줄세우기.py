### 줄 세우기 (G3)
import sys
input = sys.stdin.readline
from collections import deque

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
indegree = [0] * (V+1)
for i in range(E):
    a, b = map(int, input().split())
    G[a].append(b)
    indegree[b] += 1

start = [] # indegree == 0인 노드는 여러개일 수 있음.

for i in range(1, V+1): # indegree가 0인 노드찾기.
    if indegree[i] == 0:
        start.append(i)
        

def topology_sort(start):
    queue = deque()
    ans = []
    for s in start:    
        queue.append(s)

    while queue:
        now = queue.popleft()
        ans.append(now)
        for next in G[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)
    
    return ans

print(*topology_sort(start))