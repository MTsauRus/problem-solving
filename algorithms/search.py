import sys
sys.stdin.readline()
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
G = [[] for v in range(V+1)]
visited = [False] * (V+1)

for _ in range(E):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s) # bidirectional

def DFS(start):
    visited[start] = True
    for vertex in G[start]:
        if not visited[vertex]:
            DFS(vertex)

def BFS(start):
    queue = []
    queue.append(start)
    now = queue.pop()

    while queue:
        visited[now] = True

        for next in G[now]:
            if not visited[next]:
                queue.append(next)

num = [5, 6, 3, 4, 1, 2]

def Bsearch(num : list, key):
    num.sort()
    front = 0
    rear = len(num) - 1

    while front <= rear:
        mid = (front + rear) // 2
        if num[mid] == key:
            return mid
        
        elif num[mid] > key:
            front = mid + 1

        else:
            rear = mid - 1
    
    return -1







    

