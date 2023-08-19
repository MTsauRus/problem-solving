### K번째 수(G2)
import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

front = 1
rear = k
ans = 0

while front <= rear:

    mid = (front + rear) // 2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(N, mid // i)

    if cnt >= k:
        rear = mid - 1
        ans = mid
        
    else:
        front = mid + 1


print(ans)