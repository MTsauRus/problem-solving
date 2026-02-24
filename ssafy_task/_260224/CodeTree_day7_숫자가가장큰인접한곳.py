# 다시 짜야됨
N, M, T = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

marbles = []
for _ in range(M):
    marbles.append(tuple(map(lambda x : int(x)-1, input().split())))

marble_board = [[0]*N for _ in range(N)]

for i in range(M):
    next = marbles[i]
    marble_board[next[0]][next[1]] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for _ in range(T):
    limit = len(marbles)
    for i in range(limit):
        localMax = 0
        now = marbles.pop(0)
        mr = 0
        mc = 0
        for k in range(4):
            nr = now[0]+dr[k]
            nc = now[1]+dc[k]

            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] > localMax:
                    localMax = board[nr][nc]
                    mr = nr
                    mc = nc

        marble_board[now[0]][now[1]]-=1
        marble_board[mr][mc]+=1
        marbles.append((mr, mc))
        
    deleteList = []
    for x in range(N):
        for y in range(N):
            if marble_board[x][y] >= 2:
                for i in range(len(marbles)):
                    if marbles[i][0] == x and marbles[i][1] == y:
                        deleteList.append(i)
    
    offset = 0
    for next in deleteList:
        marbles.pop(next-offset)
        offset+=1
    
ans = 0
for i in range(N):
    for j in range(N):
        if marble_board[i][j] == 1:
            ans+=1

print(ans)