import sys
input = sys.stdin.readline
import copy
from collections import deque

K, M = map(int, input().split())
global_G = [list(map(int, input().split())) for _ in range(5)]
wall = deque(list(map(int, input().split())))
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
global_make_zero = []

def findBest():
    localSum = 0
    best_G = None
    
    # rot -> c -> r
    for rot in range(1, 4): # 1: 90 2: 180 3: 270
        for c in range(3):
            for r in range(3):
                rotated_G = rotate(r, c, rot)
                # calcScore에서 0이 나오면 종료
                tmpSum = calcScore(rotated_G)
                if localSum < tmpSum:
                    localSum = tmpSum
                    best_G = rotated_G

    return best_G


def rotate(r, c, rot):
    ret_G = copy.deepcopy(global_G)
    # 회전부위 자르기
    tmp = [[0, 0, 0] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            tmp[i][j] = global_G[r+i][c+j]
    
    rot_tmp = copy.deepcopy(tmp)
    for i in range(3):
        for j in range(3):
            if rot == 1:
                rot_tmp[i][j] = tmp[2-j][i]
            elif rot == 2:
                rot_tmp[i][j] = tmp[2-i][2-j]
            else:
                rot_tmp[i][j] = tmp[j][2-i]
    
    for i in range(3):
        for j in range(3):
            ret_G[i+r][j+c] = rot_tmp[i][j]
    
    return ret_G
        
def calcScore(G):
    score = 0
    visited = [[False]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                visited[i][j] = True
                tmpCnt = bfs(G, i, j, visited)
                if tmpCnt >= 3:
                    score += tmpCnt
    
    return score
        
def bfs(G, r, c, visited):
    dq = deque([(r, c)])
    num = G[r][c]
    
    # 나중에 0 만들 트래킹 리스트
    track = [(r, c)]
    
    cnt = 1
    while dq:
        r, c = dq.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc] and num == G[nr][nc]:
                cnt += 1
                track.append((nr, nc))
                visited[nr][nc] = True
                dq.append((nr, nc))

    # 유물임이 확정되면 현재 가치 + 0으로 만들 곳 리턴
    if cnt >= 3:
        for tup in track:
            global_make_zero.append(tup)
        return cnt
    
    # 아니면 0 리턴 (유물 못만듦)
    return 0

def sol():
    global global_G
    best_G = None
    
    for _ in range(K):
        nowScore = 0
        best_G = findBest()
        if best_G is None: 
            return
        
        global_G = copy.deepcopy(best_G)
        # 점수추가 -> 조각리필 반복
        while True:
            global_make_zero.clear()
            tmpScore = calcScore(global_G)
            
            if tmpScore == 0: break
            # 현재 iter 점수추가
            nowScore += tmpScore
            
            # 유물인거 0으로 만들기
            while global_make_zero:
                r, c = global_make_zero.pop()
                global_G[r][c] = 0
            
            # 조각 리필
            for c in range(5):
                for r in range(4, -1, -1):
                    if global_G[r][c] == 0:
                        global_G[r][c] = wall.popleft()

        print(nowScore, end=" ")

if __name__ == "__main__":
    sol()