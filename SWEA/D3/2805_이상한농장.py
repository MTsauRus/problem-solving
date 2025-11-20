### 2805. 이상한 농장 (D3)
### 브루트 포스, 구현
T = int(input())
for t in range(1, T+1):
    N = int(input())
    G = []
    for i in range(N):
        G.append(list(map(int, input().strip())))
    
    s = N//2
    e = s+1
    ans = 0
    for i in range(N//2):
        ans += sum(G[i][s:e])
        s-=1
        e+=1
    ans += sum(G[N//2])
    s+=1
    e-=1
    for i in range(N//2+1, N):
        ans += sum(G[i][s:e])
        s+=1
        e-=1
    print(f'#{t} {ans}')