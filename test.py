import sys
import heapq
input=sys.stdin.readline

N,E=map(int,input().split())
START=int(input())

graph=[[] for _ in range(N+1)]
INF=sys.maxsize
distance=[INF]*(N+1)

for _ in range(E):
  s,e,v=map(int,input().split())
  graph[s].append((e,v))

def dijkstra(start):
  q=[]
  #(cost,node)
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q:
    nowDist,nowNode=heapq.heappop(q)
    if nowDist>distance[nowNode]: continue
    for i in graph[nowNode]:
      cost=nowDist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q, (cost,i[0]))

dijkstra(START)
for i in range(1,N+1):
  if distance[i]==INF:
    print("INF")
  else:
    print(distance[i])