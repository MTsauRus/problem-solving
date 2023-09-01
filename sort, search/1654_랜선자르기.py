### 랜선 자르기 (S2)
import sys
input = sys.stdin.readline

K, need = map(int, input().split())

line = []
for _ in range(K):
    line.append(int(input()))

front = 1
rear = max(line)
while front <= rear:
    cnt = 0
    mid = (front + rear) // 2
    for l in line:
        while l - mid >= 0:
            l -= mid
            cnt += 1
    
    if cnt >= need:
        #print("front", front, mid, rear)
        ans = mid
        front = mid + 1

    else:
        #print("rear", front, mid, rear)
        rear = mid - 1

print(rear)
