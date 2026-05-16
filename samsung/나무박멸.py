import sys
input = sys.stdin.readline
from copy import deepcopy
from math import floor

N, M, K, remain = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
cantGrow = [[0]*N for _ in range(N)]
# 사방 인접
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
# 제초제 
kr = [-1, -1, 1, 1]
kc = [-1, 1, -1, 1]

def grow():
    global G
    for i in range(N):
        for j in range(N):
            tmpSum = 0
            # 나무가 있다면
            if G[i][j] >= 1:
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if 0 <= nr < N and 0 <= nc < N and G[nr][nc] >= 1:
                        tmpSum += 1
            
            G[i][j] += tmpSum
    
    return


def propagate():
    global G
    G_tmp = deepcopy(G)
    
    for i in range(N):
        for j in range(N):
            if G[i][j] >= 1:
                # 분모, 번식할 칸 수
                mo = 0
                # 번식할 자리
                site = []
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    # cantGrow: 제초제 여부, 0이면 없는거
                    if 0 <= nr < N and 0 <= nc < N and G[nr][nc] == 0 and cantGrow[nr][nc] == 0:
                        mo += 1
                        site.append((nr, nc))
                
                for r, c in site:
                    G_tmp[r][c] += floor(G[i][j] / mo)
    
    G = deepcopy(G_tmp)
    return

def selectKill():
    # tr, tc: 제초제 뿌릴 좌표
    tr = 0
    tc = 0
    localMax = 0
    
    for i in range(N):
        for j in range(N):
            if G[i][j] == -1 or G[i][j] == 0: continue
            
            killed = G[i][j]
            # 4방향에 대해
            for d in range(4):
                # 사거리 K
                for k in range(1, K+1):
                    nr = i + k*kr[d]
                    nc = j + k*kc[d] 
                    if not (0 <= nr < N and 0 <= nc < N):
                        break
                    # 벽이거나 나무없으면 그쪽 방향 탐색 끝
                    if G[nr][nc] == -1 or G[nr][nc] == 0: break
                    
                    killed += G[nr][nc]
                    
            if killed > localMax:
                tr = i
                tc = j
                localMax = killed
    
    return (tr, tc)

def kill(tr, tc):
    global cantGrow
    if G[tr][tc] <= 0: return 0
    tmpSum = G[tr][tc]
    # 먼저 중앙 칸 제초처리하고
    cantGrow[tr][tc] = remain
    G[tr][tc] = 0
    for d in range(4):
        # 사거리 K
        for k in range(1, K+1):
            nr = tr + k*kr[d]
            nc = tc + k*kc[d] 
            if not (0 <= nr < N and 0 <= nc < N): break
            cantGrow[nr][nc] = remain
            if G[nr][nc] == -1 or G[nr][nc] == 0: break
            
            # 나무 죽이기
            tmpSum += G[nr][nc]
            G[nr][nc] = 0

    return tmpSum

# 살충제 지속시간 -1
def nextYear():
    for i in range(N):
        for j in range(N):
            if cantGrow[i][j] >= 1:
                cantGrow[i][j] -= 1

def sol():
    ans = 0
    for _ in range(M):
        grow()
        propagate()
        tr, tc = selectKill()
        nextYear()
        ans += kill(tr, tc)
    
    print(ans)
    return

if __name__ == "__main__":
    sol()