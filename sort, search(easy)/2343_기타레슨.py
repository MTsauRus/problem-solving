### 기타 레슨(S1)
import sys
input = sys.stdin.readline

lecture, N = map(int, input().split())
minute = list(map(int, input().split()))

front = max(minute)
rear = sum(minute)

while front <= rear:
    cnt = 0
    sum = 0
    mid = (front + rear) // 2

    for min in minute:
        if sum + min > mid:
            cnt += 1
            sum = 0
        
        sum += min

    if sum != 0:
        cnt += 1

    if cnt <= N:
        rear = mid - 1
    
    else:
        front = mid + 1

print(front)