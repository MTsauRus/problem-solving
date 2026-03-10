### 2887 행성 터널 (P5)
### MST, 크루스칼
import sys
input = sys.stdin.readline


N = int(input())
parent = [i for i in range(N)]
rank = [0 for i in range(N)]

V = [[i]+list(map(int, input().split())) for i in range(N)]
xSort = sorted(V, key = lambda x : x[1])
ySort = sorted(V, key = lambda x : x[2])
zSort = sorted(V, key = lambda x : x[3])

edges = []
for i in range(N-1):
    edges.append((xSort[i][0], xSort[i+1][0], abs(xSort[i][1]-xSort[i+1][1])))
    edges.append((ySort[i][0], ySort[i+1][0], abs(ySort[i][2]-ySort[i+1][2])))
    edges.append((zSort[i][0], zSort[i+1][0], abs(zSort[i][3]-zSort[i+1][3])))
    
edges.sort(key = lambda x : x[2])

def find(a):
    if parent[a] == a: return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    aa = find(a)
    bb = find(b)
    if aa == bb: return False
    
    if (rank[aa] > rank[bb]):
        parent[bb] = aa
    elif (rank[aa] < rank[bb]):
        parent[aa] = bb
    else:
        parent[bb] = aa
        rank[aa] += 1
    return True

ans = 0
cnt = 0    
for edge in edges:
    if (union(edge[0], edge[1])):
        cnt += 1
        ans += edge[2]
    if cnt == N-1:
        break

print(ans)