### 21608. 상어 초등학교 (G5)
### 구현, 그래프 탐색
import sys
input = sys.stdin.readline

N = int(input())
students = []
for i in range(N**2):
    students.append(list(map(int,input().split())))
favo = dict()

G = [[0 for _ in range(N)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def find_sit(now_num):
    fit = [-1, -1] # 동점인 경우 행/열 번호 우선순위를 매기기 위함
    score_max = -1
    now_like = favo[now_num]
    
    for x in range(N):
        for y in range(N):
            if G[x][y]: continue # 이미 앉은 자리면 패스
            score = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if G[nx][ny] in now_like:
                        score += 5 # 좋아하는 사람 있으면 5점: 빈칸 4개 < 좋아하는 사람 1명
                    elif G[nx][ny] == 0:
                        score += 1 # 빈칸이면 1점
            
            if score > score_max:
                fit = [x, y]
                score_max = score
                
    return fit[0], fit[1]

def calc_score():
    tot_score = 0
    for x in range(N):
        for y in range(N):
            tmp_like_people = 0
            now_like = favo[G[x][y]]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if G[nx][ny] in now_like:
                        tmp_like_people += 1

            if tmp_like_people == 0:
                continue
            tot_score += 10**(tmp_like_people-1)

    return tot_score

for next in students:
    now_num = next[0]
    now_like = set(next[1:]) # set in 연산: 최적 O(1)
    favo.update({now_num : now_like})
    nx, ny = find_sit(now_num)
    G[nx][ny] = now_num

print(calc_score())