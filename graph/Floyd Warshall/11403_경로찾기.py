### 경로 찾기 (S1)
import sys
maxsize = sys.maxsize

V = int(input())
G = []

for _ in range(V):
    G.append(list(map(int, input().split())))
for i in range(V):
    G[i][i] = 0
for k in range(V):
    for s in range(V):
        for e in range(V):
            if G[s][k] == 1 and G[k][e] == 1:
                G[s][e] = 1

for i in range(V):
    for j in range(V):
        if G[i][j] == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()
                