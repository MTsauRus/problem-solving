import sys
input = sys.stdin.readline

R, C, Q = map(int, (input().split()))
G = []
for i in range(R):
    G.append(list(map(int, input().split())))
    
for _ in range(Q):
    r1, c1, r2, c2 = map(lambda x : int(x)-1, input().split())
    
    sq1 = G[r1][c1:c2]
    sq2 = []
    for i in range(r1, r2):
        sq2.append(G[i][c2])
    sq3 = G[r2][c1+1:c2+1]
    sq4 = []
    for i in range(r1+1, r2+1):
        sq4.append(G[i][c1])
    
    idx = 0
    for i in range(c1+1, c2+1):
        G[r1][i] = sq1[idx]
        idx+=1
    idx = 0
    for i in range(r1+1, r2+1):
        G[i][c2] = sq2[idx]
        idx+=1
    idx=0
    for i in range(c1, c2):
        G[r2][i] = sq3[idx]
        idx+=1
    idx=0
    for i in range(r1, r2):
        G[i][c1] = sq4[idx]
        idx+=1
    
    next_board = [[0]*C for _ in range (R)]

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    for i in range(R):
        for j in range(C):
            if (i < r1 or i > r2) or (j < c1 or j > c2):
                next_board[i][j] = G[i][j]
            else:
                div = 1
                tmp_sum = G[i][j]
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if (0 <= nr < R and 0 <= nc < C):
                        div += 1
                        tmp_sum += G[nr][nc]
                
                next_board[i][j] = tmp_sum // div
    
    G = next_board

for i in range(R):
    for j in range(C):
        print(G[i][j], end=" ")
    print()