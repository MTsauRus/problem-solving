### 불우이웃돕기 (G3)
import sys
input = sys.stdin.readline
from heapq import heappush, heappop
V = int(input())
E = []
total = 0
for i in range(V):
    tmp = list(input().strip())
    for j in range(V):
        if tmp[j] == '0':
            continue
        weight = ord(tmp[j])
        if 65 <= weight <= 90:
            weight -= 38
        else:
            weight -= 96
        total += weight
        if i == j:
            continue
        heappush(E, [weight, i, j])
        
parent = [i for i in range(V)]
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    if a < b:
        parent[b] = a
        
    else:
        parent[a] = b
    return True

essential = 0
edge_cnt = 0

for i in range(len(E)):
    w, a, b = heappop(E)
    if union(a, b):
        essential += w
        edge_cnt += 1

if edge_cnt == V-1:
    print(total - essential)
else:
    print(-1)
    
