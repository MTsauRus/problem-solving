### 게임 (S3)
X, Y = map(int, input().split())
Z = int(Y*100//X)
if Z >= 99:
    print(-1)
    exit(0)

front = 1
rear = 2000000001
ans = 0

while front <= rear:
    mid = (front+rear)//2
    tmp = int((Y+mid)*100/(X+mid))
    if tmp > Z:
        rear = mid - 1
    else:
        front = mid + 1
        
print(front)