### 2623. 음악프로그램 (G3)
### 위상 정렬
import sys
from collections import deque
input = sys.stdin.readline

V, N = map(int, input().split())
G = [[] for _ in range(V+1)]
indegree = [0 for _ in range(V+1)]
for i in range(N):
    l = list(map(int, input().split()))
    for j in range(1, len(l)-1):
        G[l[j]].append(l[j+1])
        indegree[l[j+1]] += 1

queue = deque()
ans = []
flag = False
for i in range(1, V+1):
    if indegree[i] == 0:
        flag = True
        queue.append(i)

while queue:
    now = queue.popleft()
    ans.append(now)
    for next in G[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

if len(ans) != V:
    print(0)
else:
    for next in ans:
        print(next)
