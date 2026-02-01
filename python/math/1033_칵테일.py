import sys
from math import gcd
input = sys.stdin.readline

N = int(input())
G = [[] for _ in range(N)]
visited = [False] * N
ratio = set()
weight = [0 for _ in range(N)]
lcm = 1

for i in range(N-1):
    a, b, p, q = map(int, input().split())
    G[a].append((b, p, q))
    G[b].append((a, q, p))
    lcm *= (p*q) //gcd(p,q)

weight[0] = lcm
def dfs(v):
    visited[v] = True
    for next in G[v]:
        if not visited[next[0]]:
            #visited[next[0]] = True
            weight[next[0]] = weight[v] * next[2] // next[1]
            dfs(next[0])
dfs(0)
gcd = gcd(*weight)
weight = list(map(lambda x : x // gcd, weight))
print(*weight)