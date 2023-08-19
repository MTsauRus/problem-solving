import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
visited = [False] * (V+1)
global cnt
cnt = 0 # count of DFS

for _ in range(E):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s) # bidirectional

def DFS(v):
    global cnt
    visited[v] = True
    for vertex in G[v]:
        if not visited[vertex]:
            cnt += 1
            DFS(vertex)

for i in range(V):
    if not visited[i]:
        cnt = 0
        DFS(i)

print(cnt)        


