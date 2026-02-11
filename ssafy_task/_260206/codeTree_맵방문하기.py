import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = []
visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(5)] 
cnt = 0
ans = 0
for i in range(R):
    board.append(list(input().strip()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
    
def bfs(board, r, c):
    global cnt
    global ans
    cnt += 1
    tot = 1
    if (board[r][c] == 'U'):
        dir = 0
    elif (board[r][c] == 'D'):
        dir = 1
    elif (board[r][c] == 'L'):
        dir = 2
    else:
        dir = 3
    nr = r + dr[dir]
    nc = c + dc[dir]

    while (0 <= nr < R and 0 <= nc < C and visited[dir][nr][nc] != cnt):
        visited[dir][nr][nc] = cnt
        tot += 1
        if (board[nr][nc] == 'U'):
            dir = 0
        elif (board[nr][nc] == 'D'):
            dir = 1
        elif (board[nr][nc] == 'L'):
            dir = 2
        else:
            dir = 3
        nr += dr[dir]
        nc += dc[dir]
    ans = max(ans, tot)

for i in range(R):
    uBoard = [a[:] for a in board]
    uBoard[i] = ['U'] * C
    dBoard = [a[:] for a in board]
    dBoard[i] = ['D'] * C
    lBoard = [a[:] for a in board]
    lBoard[i] = ['L'] * C
    rBoard = [a[:] for a in board]
    rBoard[i] = ['R'] * C
    
    for x in range(R):
        for y in range(C):
            bfs(uBoard, x, y)
            bfs(dBoard, x, y)
            bfs(lBoard, x, y)
            bfs(rBoard, x, y)

for i in range(C):
    uBoard = [a[:] for a in board]
    dBoard = [a[:] for a in board]
    lBoard = [a[:] for a in board]
    rBoard = [a[:] for a in board]
    for j in range(R):
        uBoard[j][i] = 'U'
        dBoard[j][i] = 'D'
        lBoard[j][i] = 'L'
        rBoard[j][i] = 'R'
    
    for x in range(R):
        for y in range(C):
            bfs(uBoard, x, y)
            bfs(dBoard, x, y)
            bfs(lBoard, x, y)
            bfs(rBoard, x, y)

print(ans)