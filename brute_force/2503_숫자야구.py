### 숫자 야구 (S3)
import sys
input = sys.stdin.readline

num = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and i != k:
                num.append(str(100*i+10*j+k))
ans = []

N = int(input())
for _ in range(N):
    next = list(map(str, input().split()))
    b = next[0]
    S = set()
    for a in num:
        strike, ball = 0, 0
        if a[0] in b:
            if a[0] == b[0]:
                strike += 1
            else:
                ball += 1
        if a[1] in b:
            if a[1] == b[1]:
                strike += 1
            else:
                ball += 1
        if a[2] in b:
            if a[2] == b[2]:
                strike += 1
            else:
                ball += 1
        
        # if a[0] == b[0]:
        #     strike += 1
        # elif a[0] in b:
        #     ball += 1
        # if a[1] == b[1]:
        #     strike += 1
        # elif a[1] in b:
        #     ball += 1
        # if a[2] == b[2]:
        #     strike += 1
        # elif a[2] in b:
        #     ball += 1
        if strike == int(next[1]) and ball == int(next[2]):
            S.add(a)
    ans.append(S)
    
l = set.intersection(*ans)
  
print(len(l))      
        
        
    