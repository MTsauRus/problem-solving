### 터렛(S3)
import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = ((x1-x2)**2+(y1-y2)**2)**0.5
    r1 = float(r1)
    r2 = float(r2)
    
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    
    else:
        if r1+r2 < dis:
            print(0)
        elif r1+r2 == dis:
            print(1)
        else:
            if r1 >= r2:
                br = r1
                sr = r2
            else:
                br = r2
                sr = r1
            if dis + sr < br:
                print(0)
            elif dis + sr == br:
                print(1)
            else:
                print(2)
            