### Jungle Roads (G4)
import sys
from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return a
    
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True   
    
# ord("A") == 65
while True:
    N = int(input())
    if N == 0:
        break
    parent = [i for i in range(N)]
    
    tree = []
    edges = 0
    for i in range(N-1):
        tmp = deque(input().split())
        a = ord(tmp.popleft()) - 65
        num = int(tmp.popleft())
        edges += num
        for j in range(num): # num == 0: skip
            b = ord(tmp.popleft()) - 65
            w = int(tmp.popleft())
            heappush(tree, [w, a, b])

    weights = 0
    for i in range(edges):
        w, a, b = heappop(tree)
        if union(a, b):
            weights += w
    print(weights)
        
