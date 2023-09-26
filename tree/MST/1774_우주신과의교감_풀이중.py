### 우주신과의 교감 (G3)
# Fail
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
parents = [i for i in range(V+1)]
G = []
for _ in range(V):
    a, b = map(int, input().split())
    G.append([a, b])
#G.sort()    
connected = []
for _ in range(E):
    a, b = map(int, input().split())
    apos = G[a-1]
    bpos = G[b-1]
    
    connected.append([dis, a, b])

def find(a):
    if parents[a] == a:
        return parents[a]
    
    parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False
    
    if a > b:
        parents[a] = b
    else:
        parents[b] = a
    return True


