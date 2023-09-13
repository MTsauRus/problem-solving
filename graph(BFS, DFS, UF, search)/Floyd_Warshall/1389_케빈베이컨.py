### 케빈 베이컨의 6단계 법칙 (S1)
import sys
maxsize = sys.maxsize
input = sys.stdin.readline

V, E = map(int, input().split())
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
for _ in range(E):
    s, e = map(int, input().split())
    G[s][e] = 1
    G[e][s] = 1
for i in range(1, V+1):
    G[i][i] = 0
for k in range(1, V+1):
    for s in range(1, V+1):
        for e in range(1, V+1):
            if G[s][k] != 0 and G[k][e] != 0:
                if G[s][e] == 0:
                    G[s][e] = G[s][k]+G[k][e]
                else:
                    if G[s][e] > G[s][k]+G[k][e]:
                        G[s][e] = G[s][k]+G[k][e]

min = maxsize
ans = 0
for i in range(1, V+1):
    tmp = sum(G[i][1:])
    if tmp < min:
       ans = i
       min = tmp
       
print(ans)
