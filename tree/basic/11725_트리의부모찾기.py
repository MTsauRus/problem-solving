### 트리의 부모 찾기 (S2)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
visited = [False] * (V+1)
ans = [0] * (V+1)

def dfs(a):
    #visited[a] = True
    for next in tree[a]:
        if not visited[next]:
            visited[next] = True
            ans[next] = a
            dfs(next)
dfs(1)
for next in ans[2:]:
    print(next)