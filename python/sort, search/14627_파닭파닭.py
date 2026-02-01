### 파닭파닭 (S2)
import sys
input = sys.stdin.readline  

n, N = map(int, input().split())
pa = []
for _ in range(n):
    pa.append(int(input()))

pa.sort()

front = 1
rear = 1000000000
chickens = 0
mid = (front+rear)//2
while front <= rear:
    chickens = 0
    
    for next in pa:
        chickens += next//mid
        
    if chickens < N: 
        rear = mid-1
        
    else: # 파 길이를 늘림
        front = mid+1
        
    mid = (front + rear) // 2

print(sum(pa)-mid*N)
