### 여행 가자 (G4)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V = int(input())
trip = int(input())
parent = [i for i in range(V)]
for i in range(V): # i번째 나라
    line = list(map(int, input().split()))

    for j in range(V):
        if i == j:
            continue
        if line[j] == 1:
            union(i, j)

itinerary = list(map(lambda x : int(x) - 1, input().split())) # 인덱스는 0부터 시작
ans = "YES"
for i in range(trip-1):
    if find(itinerary[i]) != find(itinerary[i+1]):
        ans = "NO"
        break

print(ans)
    




