### 친구 (S2)
import sys
input = sys.stdin.readline

N = int(input())
G = []
for i in range(N):
    G.append(list(input().strip()))
for i in range(N):
    for j in range(N):
        if i==j:
            G[i][i] = 0
            continue
        
        if G[i][j] == 'Y':
            G[i][j] = 1
        else:
            G[i][j] = 0

for k in range(N):
    for s in range(N):
        for e in range(N):
            if G[s][e] == 0 and G[s][k] == 1 and G[k][e] == 1:
                G[s][e] = 2
mx = 0
cnt = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if 0 < G[i][j] <= 2:
            cnt += 1
    if cnt > mx:
        mx = cnt
    cnt = 0
        
print(mx)
