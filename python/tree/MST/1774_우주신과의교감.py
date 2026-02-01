### 우주신과의 교감 (G3)
# Fail
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
parents = [i for i in range(V)]
pos = []
G = []

def cal_dist(a, b):
    xpos = pos[a]
    ypos = pos[b]
    dis = ((xpos[0]-ypos[0])**2+(xpos[1]-ypos[1])**2)**0.5
    return dis

def find(a):
    if parents[a] == a:
        return parents[a]
    
    parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False
    
    if a > b:
        parents[a] = b
    else:
        parents[b] = a
    return True

for _ in range(V):
    a, b = map(int, input().split())
    pos.append([a, b])
    
for i in range(V): # 거리 계산
    for j in range(i+1, V):
        dis = cal_dist(i, j)
        G.append([dis, i, j])
G.sort()

for _ in range(E):
    a, b = map(lambda x:int(x)-1, input().split())
    union(a, b)

dist = 0.0
for dis, a, b in G:
    if union(a, b):
        dist += dis
print(format(dist, ".2f"))
