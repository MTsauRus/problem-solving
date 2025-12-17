import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

left = [] # 최대 힙 (음수 저장)
right = [] # 최소 힙

for i in range(N):
    next = int(input())
    
    # 두 힙 길이가 같으면 왼쪽에 넣음
    if len(left) == len(right):
        heappush(left, -next)
        
    else: # 왼쪽 힙이 더 크면 오른쪽에 넣음
        heappush(right, next)
        
    # 오른쪽 힙이 존재하지만, 오른쪽 최솟값이 왼쪽 최댓값보다 작은 경우
    # 잘못 들어간것이므로 이를 스왑한다. 
    if right and -left[0] > right[0]:
        heappush(left, -heappop(right))
        heappush(right, -heappop(left))

    # 왼쪽 최댓값이 항상 mid이다. (짝수일 때에도 왼쪽, 작은 쪽이 mid이므로)
    print(-left[0])
