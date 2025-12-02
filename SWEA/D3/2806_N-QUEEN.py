### 2806. N-QUEEN
### 백트래킹
def is_safe(r, c):
    for i in range(1, r+1, 1):
        if c in board or board[r-i] == c-i or board[r-i] == c+i:
            return False
    return True    

def sol(r):
    global ans
    if r == N:
        ans += 1
        return
    
    for c in range(N):
        if is_safe(r, c):
            board[r] = c
            sol(r+1)
            board[r] = -1

T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [-1 for i in range(N)]
    ans = 0
    
    sol(0)
    
    print(f'#{t} {ans}')