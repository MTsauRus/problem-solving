### 1005. ACM craft (G3)
### DFS, DP 풀이
import sys
input = sys.stdin.readline
from collections import deque

def recursive(s):
    if not G[s]: # in_degree = 0인 경우. base case
        D[s] = delay[s]
        return D[s]
    if D[s] != -1: # 이미 계산한 적이 있다면 바로 리턴
        return D[s]
    max_now = 0
    for before in G[s]:
        # 선수 노드 중 최대 시간 찾기
        max_now = max(recursive(before), max_now)
    D[s] = max_now + delay[s]
    return D[s]

T = int(input())
ans = []
for t in range(T):
    V, E = map(int, input().split())
    delay = [0] + list(map(int, input().split()))
    G = [[] for i in range(V+1)]
    G_reverse = [[] for i in range(V+1)]
    D = [-1 for _ in range(V+1)] # D[i]: i번째 건물까지의 건설 시간

    for i in range(E):
        s, e = map(int, input().split())
        #G[s].append(e)
        G[e].append(s) # 역방향으로 저장
    win = int(input()) # 승리하기 위해 지어야 하는 건물
    ans.append(recursive(win))
    
for i in range(T):
    print(ans[i])
