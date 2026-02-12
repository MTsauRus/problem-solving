import sys
input = sys.stdin.readline

board = []
ans = 0

N = int(input())
for i in range(N):
    board.append(list(map(int, input().split())))

def push(dir, board):
    if dir == 0:
        for c in range(N):
            idx = 0
            for r in range(N):
                if board[r][c] != 0:
                    board[idx][c] = board[r][c]
                    if (r != idx):
                        board[r][c] = 0
                    idx += 1    
    elif dir == 1:
        for c in range(N):
            idx = N-1
            for r in range(N-1, -1, -1):
                if board[r][c] != 0:
                    board[idx][c] = board[r][c]
                    if (r != idx):
                        board[r][c] = 0
                    idx -= 1
    elif dir == 2:
        for r in range(N):
            idx = 0
            for c in range(N):
                if board[r][c] != 0:
                    board[r][idx] = board[r][c]
                    if (c != idx):
                        board[r][c] = 0
                    idx += 1
    elif dir == 3:
        for r in range(N):
            idx = N-1
            for c in range(N-1, -1, -1):
                if board[r][c] != 0:
                    board[r][idx] = board[r][c]
                    if (c != idx):
                        board[r][c] = 0
                    idx -= 1
    return board

def merge(dir, board):
    if dir == 0:
        for c in range(N):
            for r in range(N-1):
                if board[r][c] == board[r+1][c]:
                    board[r][c] = board[r][c] * 2
                    board[r+1][c] = 0
    if dir == 1:
        for c in range(N):
            for r in range(N-1, 0, -1):
                if board[r][c] == board[r-1][c]:
                    board[r][c] = board[r][c] * 2
                    board[r-1][c] = 0
    if dir == 2:
        for r in range(N):
            for c in range(N-1):
                if board[r][c] == board[r][c+1]:
                    board[r][c] = board[r][c] * 2
                    board[r][c+1] = 0
    if dir == 3:
        for r in range(N):
            for c in range(N-1, 0, -1):
                if board[r][c] == board[r][c-1]:
                    board[r][c] = board[r][c] * 2
                    board[r][c-1] = 0
    return board

def move(dir, board):
    copy_board = [row[:] for row in board]
    return push(dir, merge(dir, push(dir, copy_board)))

def calculate_max(board):
    global ans
    localMax = 0
    for i in range(N):
        tmpMax = max(board[i])

        localMax = max(tmpMax, localMax)
    ans = max(localMax, ans)

def dfs(depth, prev_board):
    if (depth == 5):
        calculate_max(prev_board)
        return
    
    for i in range(4):
        dfs(depth+1, move(i, prev_board))

dfs(0, board)
print(ans)