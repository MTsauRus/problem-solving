import sys
input = sys.stdin.readline

board = []
for i in range(4):
    board.append(list(map(int, input().split())))

dir = input().strip()

def push(dir):
    global board
    if dir == 'U':
        for c in range(4):
            idx = 0
            for r in range(4):
                if board[r][c] != 0:
                    board[idx][c] = board[r][c]
                    if (r != idx):
                        board[r][c] = 0
                    idx += 1    
    elif dir == 'D':
        for c in range(4):
            idx = 3
            for r in range(3, -1, -1):
                if board[r][c] != 0:
                    board[idx][c] = board[r][c]
                    if (r != idx):
                        board[r][c] = 0
                    idx -= 1
    elif dir == 'L':
        for r in range(4):
            idx = 0
            for c in range(4):
                if board[r][c] != 0:
                    board[r][idx] = board[r][c]
                    if (c != idx):
                        board[r][c] = 0
                    idx += 1
    elif dir == 'R':
        for r in range(4):
            idx = 3
            for c in range(3, -1, -1):
                if board[r][c] != 0:
                    board[r][idx] = board[r][c]
                    if (c != idx):
                        board[r][c] = 0
                    idx -= 1

def merge(dir):
    global board
    if dir == 'U':
        for c in range(4):
            for r in range(3):
                if board[r][c] == board[r+1][c]:
                    board[r][c] *= 2
                    board[r+1][c] = 0
    if dir == 'D':
        for c in range(4):
            for r in range(3, 0, -1):
                if board[r][c] == board[r-1][c]:
                    board[r][c] *= 2
                    board[r-1][c] = 0
    if dir == 'L':
        for r in range(4):
            for c in range(3):
                if board[r][c] == board[r][c+1]:
                    board[r][c] *= 2
                    board[r][c+1] = 0
    if dir == 'R':
        for r in range(4):
            for c in range(3, 0, -1):
                if board[r][c] == board[r][c-1]:
                    board[r][c] *= 2
                    board[r][c-1] = 0
    
push(dir)
merge(dir)
push(dir)

for l in board:
    print(*l)