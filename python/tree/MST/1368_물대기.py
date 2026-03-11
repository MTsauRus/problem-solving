### 1368. 물대기 (G2)
### MST, prim 풀이

import sys
input = sys.stdin.readline

N = int(input())

zeroRow =[100001] + [int(input()) for _ in range(N)] # 가상의 노드번호 0 -> 모든 노드로 연결된 엣지가 있다고 가정
G = [[] for _ in range(N+1)]
G[0] = zeroRow

for i in range(1,N+1):
    first = zeroRow[i]
    G[i] = [first] + list(map(int, input().split()))

start = -1
dist = [float('inf')] * (N+1)
visited = [False] * (N+1)
ans = 0
nodeCnt = 0
dist[0] = 0

while nodeCnt < N+1:
    nodeCnt += 1
    
    localMin = float('inf')
    now = -1
    
    # MST와 가장 가까운 다음 노드 찾기
    for i in range(N+1):
        if not visited[i] and dist[i] < localMin:
            localMin = dist[i]
            now = i
        
    visited[now] = True
    ans += dist[now]
    
    # dist 업데이트하기
    for i in range(N+1):
        if not visited[i]:
            if dist[i] > G[now][i]:
                dist[i] = G[now][i]
                
print(ans)