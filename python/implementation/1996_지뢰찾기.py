### 1996. 지뢰 찾기 (S5)
### 그래프 탐색, 구현
import sys
input = sys.stdin.readline

N = int(input())
G = []
for i in range(N):
    G.append(list(input().strip()))
    
ans = [[0 for _ in range(N)] for _ in range(N)]
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

for r in range(N):
    for c in range(N):
        if G[r][c] != '.':
            ans[r][c] = '*'
            continue
        
        tmp_sum = 0
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and G[nr][nc] != '.':
                tmp_sum += int(G[nr][nc])
                if tmp_sum >= 10:
                    ans[r][c] = 'M'
                    break
                
        if ans[r][c] != 'M':
            ans[r][c] = tmp_sum

for next in ans:
    for ch in next:
        print(ch, end="")
    print()