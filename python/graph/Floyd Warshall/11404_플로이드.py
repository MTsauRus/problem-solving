### 플로이드 (G4)
import sys
maxsize = sys.maxsize
input = sys.stdin.readline

V = int(input())
E = int(input())
G = [[maxsize for _ in range(V+1)] for _ in range(V+1)]
for i in range(1, V+1):
    G[i][i] = 0 

for _ in range(E):
    s, e, w = map(int, input().split())
    if G[s][e] > w:
        G[s][e] = w
    
for k in range(1, V+1):
    for s in range(1, V+1):
        for e in range(1, V+1):
            if G[s][e] > G[s][k] + G[k][e]:
                G[s][e] = G[s][k] + G[k][e]

for i in range(1, V+1):
    for j in range(1, V+1):
        if G[i][j] == maxsize:
            print(0, end=" ")
        else:
            print(G[i][j], end=" ")
    print()