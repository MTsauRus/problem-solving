### 종이의 개수 (S2)
### 재귀, 구현
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
G = []
ans = [0, 0, 0] # 0, 1, -1
for i in range(n):
    G.append(list(map(int, input().split())))
    
def sol(x1, x2, y1, y2):
    num = G[x1][y1]
    for nx in range(x1, x2):
        for ny in range(y1, y2):
            if G[nx][ny] != num:
                
                ratiox = (x2-x1)//3
                ratioy = (y2-y1)//3
                
                dx = [x1, x1+ratiox, x1+(ratiox*2), x2]
                dy = [y1, y1+ratioy, y1+(ratioy*2), y2]
                for i in range(3):
                    for j in range(3):
                        sol(dx[i], dx[i+1], dy[j], dy[j+1])
                return
            
    ans[num] += 1
    return

sol(0, n, 0, n)
print(ans[-1])
print(ans[0])
print(ans[1])