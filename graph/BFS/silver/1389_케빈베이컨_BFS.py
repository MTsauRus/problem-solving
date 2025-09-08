### 케빈 베이컨의 6단계 법칙 (BFS 풀이) (S1)
import sys
input = sys.stdin.readline
from collections import deque

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
ans = sys.maxsize
idx = sys.maxsize
for _ in range(E):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    
def bfs(start):
    queue = deque()
    visited = [False] * (V+1)
    queue.append(start)
    bacon = [0 for _ in range(V+1)]
    while queue:
        now = queue.popleft()
        for next in G[now]:
            if not visited[next]:
                bacon[next] += bacon[now] + 1
                visited[next] = True
                queue.append(next)
                
    return sum(bacon)

for i in range(1, V+1):
    tmp = bfs(i)
    if ans > tmp:
        ans = tmp
        idx = i
        
print(idx)
                