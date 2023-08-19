### 트리의 지름 (G3) ###
import sys
input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]

for _ in range(1, V+1):
    j = 1
    tmp = list(map(int, input().split()))
    vertex = tmp[0] # 정점이 순서대로 들어오지 않는 경우
    while tmp[j] != -1:
        tree[vertex].append((tmp[j], tmp[j+1]))
        j += 2


def BFS(start):
    visited = [False] * (V+1)
    queue = []
    queue.append(start)
    distance_list = [0 for i in range(V+1)] # 최대 거리 노드 저장용

    while queue:
        now = queue.pop(0)
        visited[now] = True

        for next in tree[now]: # next: tuple
            if not visited[next[0]]:
                queue.append(next[0])
                distance_list[next[0]] += distance_list[now] + next[1] # 현재 총 이동거리를 더해줌.

    return (distance_list.index(max(distance_list)), max(distance_list))

start, _ = BFS(1)
_, ans = BFS(start)
print(ans)