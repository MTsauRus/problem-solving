### 1005. ACM craft(G3)
### 위상 정렬 풀이

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    delay = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(V + 1)]
    in_degree = [0] * (V + 1) # 들어오는 차수
    
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        in_degree[e] += 1 # 진입 차수를 세자
        
    win_node = int(input())
    
    # DP 테이블. 각 건물이 완성되는 최소 시간을 저장.
    # 초기값은 자기 자신이 지어지는 시간.
    dp_table = [0] + delay[1:]
    
    queue = deque()
    # 진입 차수가 0인 노드들을 큐에 삽입
    for i in range(1, V + 1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        
        for next_node in graph[now]:
            # DP 점화식: 다음 건물의 완료 시간 = max(기존 값, 현재 건물 완료 시간 + 다음 건물 딜레이)
            dp_table[next_node] = max(dp_table[next_node], dp_table[now] + delay[next_node])
            
            # 진입 차수 감소
            in_degree[next_node] -= 1
            
            # 진입 차수가 0이 되면 큐에 추가 (모든 진입 차수를 고려했으므로)
            if in_degree[next_node] == 0:
                queue.append(next_node)
                
    print(dp_table[win_node])