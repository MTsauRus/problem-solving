### 주유소 (S3)
import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
dist.append(0)
cost = list(map(int, input().split()))
ans = 0
now = 0
next = 1
tmp = dist[0] * cost[0]
while now < N:
    if cost[now]*dist[next] > cost[next]*dist[next]: # 다음이 최소인 경우
        ans += tmp
        tmp = cost[next]*dist[next]
        now = next
        next += 1
    else: # 현재가 최소인 경우
        tmp += cost[now]*dist[next]
        next += 1
    
    if next == N:
        ans += tmp
        break

print(ans)
