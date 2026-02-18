T = int(input())
def cal_max(i, j, tmp_list, depth, sum, powSum):
    global max_map, M, C
    if (depth == M):
        if (sum <= C):
            max_map[i][j] = max(max_map[i][j], powSum)
        return
    
    cal_max(i, j, tmp_list, depth+1, sum+tmp_list[depth], powSum+tmp_list[depth]**2)
    cal_max(i, j, tmp_list, depth+1, sum, powSum)
    
ansList = []
for t in range(1, T+1):
    # N: 맵크기, M: 선택가능한 개수, C: 최대벌꿀양
    N, M, C = map(int, input().split())
    
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
        
    max_map = [[0] * (N-M+1) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            tmp_list = board[i][j:j+M]
            cal_max(i, j, tmp_list, 0, 0, 0)
    
    ans = 0
    for i in range(N):
        for j in range(N-M+1):
            localMax = max_map[i][j]
            for x in range(i, N):
                if (i == x):
                    for y in range(j+M, N-M+1):
                        ans = max(localMax+max_map[x][y], ans)
                else:
                    for y in range(N-M+1):
                        ans = max(localMax+max_map[x][y], ans)

    ansList.append(ans)
for i in range(T):
    print(f"#{i+1} {ansList[i]}")