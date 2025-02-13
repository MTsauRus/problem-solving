### 유레카 이론 (B1)
import sys
input = sys.stdin.readline

tri = []
i = 1
next = 0
ans = []
while True:
    next = i*(i+1)//2
    if next > 1000:
        break
    
    tri.append(next)
    i += 1

def foo(now):
    for i in range(len(tri)):
        if tri[i] > now:
            break
        for j in range(len(tri)):
            if tri[j] > now:
                break
            for k in range(len(tri)):
                if tri[k] > now:
                    break
                tmp = tri[i]+tri[j]+tri[k]
                if tmp == now:
                    return 1
    return 0
                
n = int(input())
for _ in range(n):
    now = int(input())
    print(foo(now))
    
    
    
