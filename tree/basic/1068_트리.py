### 트리 (G5)
### 그래프 탐색
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V)]
edge = list(map(int, input().split()))
root = -1
for i in range(V):
    if edge[i] == -1:
        root = i
        continue
    tree[edge[i]].append(i)
    tree[i].append(edge[i])
    
delete = int(input())

visited = [False] * V
global ans
ans = 0
def dfs(a):
    child = 0
    global ans
    visited[a] = True
    for next in tree[a]:
        if next != delete and not visited[next]:
            dfs(next)
            child += 1
    if child == 0: # 자식 노드가 없음 == 리프 노드
        ans += 1

if delete == root:
    print(0)
else:
    dfs(root)
    print(ans)