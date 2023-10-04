### 도시 분할 계획 (G4)
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
V, E = map(int, input().split())
edges = []
parent = [i for i in range(V+1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    heappush(edges, [w, a, b])
    
def find(a):
    if a == parent[a]:
        return parent[a]
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
    return True

ans = 0
length = 0
for i in range(E):
    w, a, b = heappop(edges)
    if union(a, b):
        length += 1
        if length <= V-2:
            ans += w
print(ans)