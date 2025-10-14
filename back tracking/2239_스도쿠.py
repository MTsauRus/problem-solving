### 2239 스도쿠 (G4)
### 구현, 백트래킹
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

G = [list(map(int, input().strip())) for _ in range(9)]
zeros = []
check_rows = [[False for _ in range(10)] for _ in range(10)] # [row][num]
check_cols = [[False for _ in range(10)] for _ in range(10)] # [col][num]
check_squares = [[False for _ in range(10)] for _ in range(10)] #[square][num]

def check(r, c, num):
    return check_rows[r][num] or check_cols[c][num] or check_squares[(r//3)*3+(c//3)][num]

def check_true(r, c, num):
        check_rows[r][num] = True
        check_cols[c][num] = True
        check_squares[(r//3)*3+(c//3)][num] = True
        
def check_false(r, c, num):
        check_rows[r][num] = False
        check_cols[c][num] = False
        check_squares[(r//3)*3+(c//3)][num] = False
for r in range(9):
    for c in range(9):
        if G[r][c] == 0:
            zeros.append([r, c])
        else:
            check_true(r, c, G[r][c])

def sol(idx):
    if idx == len(zeros):
        for row in G:
            print("".join(map(str, row)))
        exit(0)
    now_r, now_c = zeros[idx]
    for i in range(1, 10):
        if not check(now_r, now_c, i): # 현재 넣은 숫자가 유효하면
            check_true(now_r, now_c, i)
            G[now_r][now_c] = i
            sol(idx+1)
            check_false(now_r, now_c, i)
            G[now_r][now_c] = 0
sol(0)