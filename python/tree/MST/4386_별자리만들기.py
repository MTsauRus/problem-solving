### 별자리 만들기 (G3)
### MST
import sys
from heapq import heappush, heappop
from math import comb
input = sys.stdin.readline

V = int(input())
G = []
parent = [i for i in range(V+1)]
star = []
for i in range(V): # star input으로 받기
    a, b = map(float, input().split())
    star.append([a, b])
for i in range(V):
    a1, a2 = star[i][0], star[i][1]
    for j in range(i+1, V):
        b1, b2 = star[j][0], star[j][1]
        dist = ((a1-b1)**2+(a2-b2)**2)**0.5
        heappush(G, [dist, i+1, j+1]) # 별 사이의 거리를 그래프에 넣자

def find(node):
    if node == parent[node]: # 현재 노드가 부모 노드와 같다면
        return parent[node] # 본인이 부모임
    
    parent[node] = find(parent[node]) # 경로 압축
    return parent[node]

def union(a, b):
    a = find(a) # a의 부모
    b = find(b) # b의 부모
    
    if a == b: # 조상이 같은 경우. 연결 시 사이클
        return False
    if a < b:
        parent[b] = a # 작은 노드 번호를 부모로 하자.
    else:
        parent[a] = b
        
    return True # 사이클이 존재하지 않는다. 정상적으로 union

ans = 0
for i in range(comb(V, 2)):
    w, a, b = heappop(G)
    if union(a, b):
        ans += w
print(f'{ans:.2f}')
        
