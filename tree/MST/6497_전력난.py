### 전력난 (G4)
import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappop, heappush

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a, b = find(a), find(b)
    if a == b: 
        return False
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b
    return True

while True:
    V, E = map(int, input().split())
    if V == 0 and E == 0:
        break
    parent = [i for i in range(V)]
    G = []
    total = 0
    for i in range(E):
        a, b, w = map(int, input().split())
        heappush(G, [w, a, b])
        total += w
    
    cost = 0
    for i in range(E):
        w, a, b = heappop(G)
        if union(a, b):
            cost += w
    print(total - cost)

    