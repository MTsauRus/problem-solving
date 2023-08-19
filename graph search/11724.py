import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
visited = [False] * V
G = [[] for _ in range(V)]
global isFriend
isFriend = False

for i in range(E):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

def DFS(v, cnt):
    global isFriend # 재귀가 4번 이상 진행되었으면 True

    visited[v] = True
    if cnt >= 4:
        isFriend = True
        return
    
    for vertex in G[v]:
        if not visited[vertex]:
            DFS(vertex, cnt + 1)
            visited[vertex] = False
    


for v in range(V):
    visited = [False] * V
    DFS(v, 0)
    if isFriend:
        break
    isFriend = False

if isFriend:
    print(1)
else:
    print(0)