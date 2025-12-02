### 1220. magnetic (S3)
T = 10
for t in range(1, T+1):
    G = []
    N = int(input())
    for i in range(N):
        G.append(list(map(int, input().split())))

    G_rev = ['' for _ in range(N)]
    for i in range(N): # col
        for j in range(N): # row
            if G[j][i] == 0:
                continue
            G_rev[i]+=str(G[j][i])
    
    ans = 0
    for next in G_rev:
        for idx in range(len(next)-1):
            if next[idx:idx+2] == '12':
                ans += 1
    print(f'#{t} {ans}')