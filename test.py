### N-Queen (G4)
### 백트래킹 알고리즘
import sys
input = sys.stdin.readline

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
global ans
ans = 0

def is_safe(board, r, c, N):
    # 왼쪽 대각선 위 방향
    for i, j in zip(range(r, -1, -1), range(c, -1,  -1)):
        if board[i][j] == 1: # 이미 퀸이 있다면
            return False
    # 오른쪽 대각선 위 방향
    for i, j in zip(range(r, -1, -1), range(c, N, 1)):
        if board[i][j] == 1: # 이미 퀸이 있다면
            return False
    # 수직 위 방향
    for i in range(r, -1, -1):
        if board[i][c] == 1:
            return False
    # 이 곳에 놓아도 안전할 때
    return True

def solve(board, r, N):
    global ans
    if r == N: # r == N-1일 때 퀸을 놓았다 -> 성공 += 1
        ans += 1
        return
        
    for c in range(0, N, 1):
        if is_safe(board, r, c, N):
            board[r][c] = 1
            solve(board, r+1, N)
            board[r][c] = 0

solve(board, 0, N)
print(ans)