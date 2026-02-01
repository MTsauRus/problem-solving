### 저울 (G4)
import sys
input = sys.stdin.readline

V = int(input())
E = int(input())
edge = [[0 for i in range(V+1)] for i in range(V+1)]
for i in range(E):
    s, e = map(int, input().split())
    edge[s][e] = '>'
    edge[e][s] = '<'

# for i in range(1,V+1):
#     print(edge[i][1:])
    
for i in range(1, V+1):
    edge[i][i] = 0

for k in range(1, V+1):
    for s in range(1, V+1):
        for e in range(1, V+1):
            if s == e:
                continue
            
            if edge[s][k] == '>' and edge[k][e] == '>':
                edge[s][e] = '>'
            elif edge[s][k] == '<' and edge[k][e] == '<':
                edge[s][e] = '<'
                
cnt = 0
for i in range(1,V+1):
    for j in range(1, V+1):
        if edge[i][j] == 0 and i != j:
            cnt += 1
    print(cnt)
    cnt = 0