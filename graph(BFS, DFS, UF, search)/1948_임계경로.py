### 임계경로 (P5)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

V = int(input())
E = int(input())
G = [[] for v in range(V+1)]
G_R = [[] for v in range(V+1)]
minute = [0] * (V+1)
indegree = [0] * (V+1)

for i in range(E):
    a, b, dis = map(int, input().split())
    G[a].append((b, dis))
    G_R[b].append((a, dis))
    indegree[b] += 1

start, end = map(int, input().split())

def topology_sort(start):
    queue = deque()
    queue.append(start)
    
    while queue:
        now = queue.popleft()
        for next in G[now]:
            indegree[next[0]] -= 1
            minute[next[0]] = max(minute[next[0]], minute[now] + next[1])
            if indegree[next[0]] == 0:
                queue.append(next[0])
topology_sort(start)
print(minute[end])

def topology_sort_reverse(end):
    queue = deque()
    queue.append(end)
    ans = 0
    visited = [False] * (V+1)
    visited[end] = True

    while queue:
        now = queue.popleft()
        for next in G_R[now]:
            if minute[now] == minute[next[0]] + next[1]:
                ans+=1
                if not visited[next[0]]:
                    queue.append(next[0])
                    visited[next[0]] = True
    return ans

print(topology_sort_reverse(end))
