### 트리의 지름 (G2) ###
import sys
input = sys.stdin.readline

V = int(input())
tree = [[] for v in range(V+1)]
max_edge = (0, 0) # 최대 거리 edge. BFS의 시작점이다.
global visited
visited = [False] * (V+1)

for _ in range(V):
    tmp = list(map(int, input().split()))
    vertex = tmp[0] # tmp리스트의 맨 앞은 현재 정점을 의미
    i = 1
    while tmp[i] != -1:
        tree[vertex].append((tmp[i], tmp[i+1])) # (연결된 정점번호, 거리)
        if tmp[i+1] > max_edge[1]:
            max_edge = (tmp[i], tmp[i+1]) # 길이가 가장 큰 edge update
        i += 2


def BFS(start): # start: vertex num
    global visited
    queue = []
    distance = 0 # 트리의 지름
    visited[start] = True
    queue.append(start)
    while queue:
        maxList = [] # 각 분기에서 최댓값을 구하기 위한 리스트
        now = queue.pop(0) # now: vertex num

        for next in tree[now]: # next:(v, distance)
            if not visited[next[0]]:
                maxList.append(next)


        if maxList: # maxList에 값이 하나라도 있다면
            max_next = max(maxList, key = lambda x : x[1]) # 최대 길이 엣지를 가진 노드 결정
            queue.append(max_next[0]) # vertex number
            distance += max_next[1] # += 엣지 길이
            visited[max_next[0]] = True

        maxList.clear()
    return distance

ans = []
#leaf = []
for i in range(1, V+1):
    if len(tree[i]) == 1: # leaf node
        visited = [False] * (V+1)
        ans.append(BFS(i))
        #leaf.append(i)
    
#todo = max(leaf, key = lambda x : tree[x][0][1])


print(max(ans))