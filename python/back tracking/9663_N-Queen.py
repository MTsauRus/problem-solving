### N-Queen (G4)
### 백트래킹 알고리즘
import sys
input = sys.stdin.readline

N = int(input())
row = [-1] * N # row[0] = 1 : 각 row의 몇 번째 col에 퀸이 놓여있는지. 즉, (0, 1)
global ans
ans = 0

def is_safe(row, r, c):
    for i in range(r):
        if row[i] == c or row[i] == c - (r - i) or row[i] == c + (r - i):
            return False
    return True

def solve(r):
    global ans
    if r == N: # r == N-1일 때 퀸을 놓았다 -> 성공 += 1
        ans += 1
        return
        
    for c in range(N):
        before = row[r]
        if is_safe(row, r, c):
            row[r] = c
            solve(r+1)
            row[r] = before

solve(0)
print(ans)