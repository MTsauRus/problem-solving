### Minimum Spanning Tree (Kruskal, nondirectional)
### time complexity: O(ElgE)
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
G = []
parent = [i for i in range(V+1)]
for i in range(E):
    a, b, w = map(int, input().split()) # edge list로 저장
    G.append([w, a, b])

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

for w, a, b in G:
    if union(a, b):
        weights += w
        
print(weights)
    
