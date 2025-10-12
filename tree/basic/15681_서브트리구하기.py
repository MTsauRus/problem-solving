### 15681 트리와 쿼리 (G5)
### 트리
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
parents = [0 for _ in range(N+1)]
childs = [0 for _ in range(N+1)] # 자식 수
V = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e = map(int, input().split())
    V[s].append(e)
    V[e].append(s)
parents[R] = R # 루트는 자기 자신이 부모

def make_tree(now_vertex, now_parent):
    for next in V[now_vertex]:
        if next != now_parent:
            parents[next] = now_vertex
            make_tree(next, now_vertex)
            
def count_child(now_vertex):
    childs[now_vertex] = 1 # 자기 자신도 포함
    for next in V[now_vertex]:
        if parents[next] == now_vertex:
            count_child(next)
            childs[now_vertex] += childs[next]
    
make_tree(R, R)
count_child(R)

queries = [int(input()) for _ in range(Q)]
for next in queries:
    print(childs[next])