### 20040.사이클 게임(G4)
### 유니온 파인드
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
parents = [i for i in range(V+1)]

def find(a):
    if a == parents[a]: # 루트이면
        return parents[a]
    parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False # 사이클
    
    if a < b:
        parents[b] = a # 작은 값을 부모로
    else:
        parents[a] = b
    return True
        
def sol():
    for i in range(1, E+1):
        s, e = map(int, input().split())
        if not union(s, e):
            return i
    return 0

print(sol())
        