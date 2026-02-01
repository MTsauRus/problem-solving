### 네트워크 연결 (G4)
import sys
input = sys.stdin.readline

V = int(input())
E = int(input())
G = []
parent = [i for i in range(V+1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    G.append([w, a, b])
G.sort()
def find(a):
    if parent[a] == a:
        return a
    
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False # cycle
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True

weights = 0
for w, a, b in G:
    if union(a,b):
        weights += w

print(weights)
    