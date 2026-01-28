### 타임머신 (G4)
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
edge = []
dist = [sys.maxsize] * (V+1)
dist[1] = 0

for i in range(E):
    a, b, w = map(int, input().split())
    edge.append((a, b, w)) # edgeList
    
for i in range(E-1):
    for a, b, w in edge:
        if dist[a] != sys.maxsize and dist[b] > dist[a] + w:
            dist[b] = dist[a] + w
    
cycle = False

for a, b, w in edge:
    if dist[a] != sys.maxsize and dist[b] > dist[a] + w:
        cycle = True
           
if cycle:
    print(-1)
else:
    for i in range(2, V+1):
        if dist[i] == sys.maxsize:
            print(-1)
        else:
            print(dist[i])
