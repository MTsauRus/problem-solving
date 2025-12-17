### 1655. 가운데를 말해요 (G2)
### 우선순위 큐
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
left = [] # mid보다 작음, 최대 힙
right = [] # mid보다 큼, 최소 힙

mid = int(input()) # 첫 값이 mid
print(mid) 

next = int(input())
if next>=mid:
    heappush(right, next)
    print(mid)
else:
    heappush(right, mid)
    mid=next
    print(mid)
    

for i in range(3, N+1): # 3번째 수부터 시작
    next = int(input())
    # print(left, right)
    # print(f'i = {i}, mid = {mid}, next = {next}')
    if i%2 == 0: # 짝수번째일 때 (각 힙의 길이가 동일할 때)
        if next>=mid: # 같거나 크다면 오른쪽으로 보내고
            heappush(right, next) 
            print(mid) # mid는 그대로
        else: # 작다면
            heappush(left, -next) # 왼쪽에 next를 넣고
            heappush(right, mid) # 기존 mid를 오른쪽으로 보내고
            mid = -heappop(left) # 왼쪽의 최댓값을 mid로 선출 (왼쪽은 최대힙이므로 음수)
            print(mid)
    
    else: # 홀수번째일 때 (left 힙이 더 작을 때)
        if next<=mid: # 같거나 작다면 왼쪽으로 보내고
            heappush(left, -next) # 최대힙이므로
            print(mid) # mid는 그대로
        else: # 크다면
            heappush(right, next) # 오른쪽에 next를 넣고
            heappush(left, -mid) # 기존 mid를 왼쪽에 보내고
            mid = heappop(right) # 새 mid는 오른쪽에서 가장 작은 값
            print(mid)
            
