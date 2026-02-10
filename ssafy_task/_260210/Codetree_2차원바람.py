import sys
input = sys.stdin.readline

R, C, Q = map(int(input().split()))
G = []
for i in range(R):
    G.append(list(map(int, input().split())))
    
for i in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    
    sq1 = G[r1][c1:c2+1]
    sq2 = []
    for j in range(r1, r2):
        sq2.append(G[j][c2])
    sq3 = G[r1+1][]