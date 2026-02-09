import sys
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(depth, localCore, localLine):
    global board
    global globalCore
    global globalLine
    global coreList
    global N
    
    if depth == len(coreList):
        if globalCore > localCore:
            return
        elif globalCore == localCore:
            globalLine = min(globalLine, localLine)
            return
        else:
            globalCore = localCore
            globalLine = localLine
            return
    
    r, c = coreList[depth]

    for i in range(4):
        iterLine = 0
        nr = r + dr[i]
        nc = c + dc[i]
        moveList = []
        while (0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0):
            moveList.append((nr, nc))
            iterLine += 1
            nr += dr[i]
            nc += dc[i]

        
        if nr == -1 or nr == N or nc == -1 or nc == N: # 끝까지 도달 -> 칠하고 넘김
            for next in moveList:
                board[next[0]][next[1]] = 2
            
            dfs(depth+1, localCore+1, localLine + iterLine)
        
        # 원상복구
        for next in moveList:
            board[next[0]][next[1]] = 0
    
    dfs(depth+1, localCore, localLine)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = []
    coreList = []
    for i in range(N):
        board.append(list(map(int, input().split())))
        
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                if 1 <= i < N-1 and 1 <= j < N-1:
                    coreList.append((i, j))
                
    globalCore = 0
    globalLine = 145
    
    dfs(0, 0, 0)
    print(f"#{t} {globalLine}")