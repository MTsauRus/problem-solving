### 게임 개발 (G3)
import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
times = [0] * (V+1)
ans = [0] * (V+1)
indegree = [0] * (V+1)
G = [[] for _ in range(V+1)]
for i in range(1, V+1):
    query = list(map(int, input().split()))
    times[i] = query[0]
    j = 1
    while query[j] != -1:
        G[query[j]].append(i)
        indegree[i] += 1
        j += 1

def topology_sort():
    queue = deque()
    for i in range(1, V+1):
        if indegree[i] == 0:
            queue.append(i)
            
    while queue:
        now = queue.popleft()
        for next in G[now]:
            indegree[next] -= 1
            ans[next] = max(ans[next], ans[now]+times[now])
            #ans[next] = ans[now] + times[now]
            if indegree[next] == 0:
                queue.append(next)
                
    for i in range(1 ,V+1):
        ans[i] += times[i]

topology_sort()
for i in range(1, V+1):
    print(ans[i])