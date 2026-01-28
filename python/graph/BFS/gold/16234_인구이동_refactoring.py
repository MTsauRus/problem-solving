import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

day = 0 # 인구 이동이 발생한 총 일수

while True:
    visited = [[False] * N for _ in range(N)]
    is_moved = False # 하루 동안 인구 이동이 한 번이라도 있었는지 체크

    # 매일 모든 칸을 순회
    for i in range(N):
        for j in range(N):
            # 아직 방문하지 않은 나라에서만 연합 탐색 시작
            if not visited[i][j]:
                visited[i][j] = True
                queue = deque([(i, j)])
                union = [(i, j)] # 연합에 속한 나라들의 좌표
                population_sum = graph[i][j] # 연합의 총 인구 수

                # BFS로 국경이 열리는 모든 인접 국가를 탐색해 연합을 형성
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            # 두 나라의 인구 차이가 L명 이상, R명 이하인지 확인
                            if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                union.append((nx, ny))
                                population_sum += graph[nx][ny]
                
                # BFS 종료 후, 형성된 연합이 2개국 이상이면 인구 이동 처리
                if len(union) > 1:
                    is_moved = True
                    avg_population = population_sum // len(union)
                    for ux, uy in union:
                        graph[ux][uy] = avg_population

    # 하루 동안 인구 이동이 전혀 없었다면 종료
    if not is_moved:
        break
        
    day += 1

print(day)