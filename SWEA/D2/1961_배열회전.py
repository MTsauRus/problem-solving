T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(input().split()))
    
    ansA = [[0 for _ in range(N)] for _ in range(N)]
    ansB = [[0 for _ in range(N)] for _ in range(N)]
    ansC = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            ansA[i][j] = arr[N-1-j][i]
            ansB[i][j] = arr[N-1-i][N-1-j]
            ansC[i][j] = arr[j][N-1-i]
            
    ans = []
    for i in range(N):
        tmp = ""
        for j in range(N):
            tmp += (ansA[i][j])
        tmp += (" ")
        for j in range(N):
            tmp += (ansB[i][j])
        tmp += (" ")
        for j in range(N):
            tmp += (ansC[i][j])
        ans.append(tmp)
    
    print(f'#{t}')
    for i in range(N):
        print(ans[i])