### 1202. 보석 도둑 (G2)
### 그리디, 우선순위 큐
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

bags = []
gems = []
values = []
weights = []
N, K = map(int, input().split()) # N: 보석 수, K: 가방 수
for n in range(N):
    w, v = map(int, input().split())
    heappush(gems, [w, -v])
    heappush(weights, w)

    
for k in range(K):
    heappush(bags, int(input())) # 가방 오름차순 정렬

ans = 0

for k in range(K):
    now_bag = heappop(bags)

    while True:
        if not gems: # 사용 가능한 보석이 없다면 (모두 values에 들어갔다면)
            break
        
        now_gem = heappop(gems)
        if now_gem[0] > now_bag:
            heappush(gems, now_gem) # 뽑았는데 가방보다 크면 다시 넣어주고 나가자.
            break
        
        heappush(values, now_gem[1]) # 현재 가방 무게에서 사용 가능한 보석의 가치를 내림차순으로 저장
    
    if len(values) == 0: # 현재 가방보다 작은 보석이 없다면
        continue
    ans += -heappop(values) # 현재 허용하는 무게의 최대 가치를 pop
    
print(ans)