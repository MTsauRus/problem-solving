### 집합의 표현 (G5)
import sys
input = sys.stdin.readline
sys.setrecursionlimit (10**6)


def find(a):
    if parent[a] == a:
        return a
    
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
for _ in range(M):
    query, a, b = map(int, input().split())
    if query == 0:
        union(a, b)

    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
