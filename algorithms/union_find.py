import sys
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n)]
rank = [1 for i in range(n)]

def find(node):
    if node == parent[node]:
        return node
    
    parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    
    if a < b: # 부모 노드의 노드번호가 작음. 
        parent[b] = a

    else:
        parent[a] = b


# rank version
# def union(a, b):
#     a = find(a)
#     b = find(b) # 각 노드의 부모를 찾음.

#     if a == b:
#         return # 부모가 같다: 이미 같은 트리임.
    
#     if rank[a] > rank[b]: # 더 작은 트리를 큰 트리로 합친다.
#         a, b = b, a

#     parent[a] = b

#     if rank[a] == rank[b]:
#         rank[b] += 1 # 트리의 높이가 같은 경우, 부모 트리의 길이 + 1