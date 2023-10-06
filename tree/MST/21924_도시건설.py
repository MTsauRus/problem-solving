### 도시 건설 (G4)
### time complexity: O(ElgE)
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

V, E = map(int, input().split())
G = []
sum = 0
parent = [i for i in range(V+1)]
for i in range(E):
    a, b, w = map(int, input().split()) # edge list로 저장
    heappush(G, [w, a, b])
    sum += w

def find(node): # 부모 찾기
    if node == parent[node]:
        return parent[node]
    
    parent[node] = find(parent[node]) # 경로 압축
    return parent[node]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b: # 조상이 같은 경우: 연결 시 사이클 발생
        return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
    return True # 사이클이 없음. 정상적으로 union

# 가중치 오름차순으로 그래프를 정렬하자. 
G.sort()
weights = 0 # sum of MST weights

for i in range(E):
    w, a, b = heappop(G)
    if union(a, b):
        weights += w
        
tmp = find(1)
flag = True
for i in range(2, len(parent)):
    if find(i) != tmp:
        flag = False
        
if flag:
    print(sum - weights)
else:
    print(-1)
