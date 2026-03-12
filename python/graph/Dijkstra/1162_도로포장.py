### 1162. 도로포장 (P5)
### 다익스트라
import sys
input = sys.stdin.readline

V, E, K = map(int, input().split())
G = [[] for _ in range(E+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    G[s].append((w, e))
    G[e].append((w, s))
    
dist = [[float('inf')]*(V+1) for _ in range(K)]

