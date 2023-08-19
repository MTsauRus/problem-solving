import sys
from math import gcd
from functools import reduce
input = sys.stdin.readline

N = int(input())
G = [[] for _ in range(N)]
visited = [False] * N
next_node = []
ratio = set()
    
for i in range(N-1):
    a, b, p, q = map(int, input().split())
    G[a].append((b, p, q))
    G[b].append((a, q, p))

def dfs(v):
    visited[v] = True
    next_node.append(v)
    for next in G[v]:
        if not visited[next[0]]:
            ratio.update([next[1], next[2]])
            dfs(next[0])

dfs(0)
res = [0 for _ in range(N)]
lcm = reduce(lambda x, y : x*y//gcd(x,y), ratio)
res[0] = lcm # 0번부터 탐색
print(lcm)

visited2 = [False] * N
def dfs2(v):
    now = v
    visited2[now] = True
    for next in G[now]:
        print(res)
        
        if not visited2[next[0]]:
            res[next[0]] = res[now] * next[2] // next[1]
            dfs2(next[0])

dfs2(0)
final_lcm = reduce(gcd, res)
for i in res:
    print(i// final_lcm, end=" ")




    

