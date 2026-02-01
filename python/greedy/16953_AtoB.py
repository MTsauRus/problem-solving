### A -> B (S2)
### 그리디

import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())
ans = 1
while True:
    if b%10 == 1:
        b //= 10
        ans += 1
        
    elif b % 2 == 0:
        b //= 2
        ans += 1
        
    else:
        ans = -1
        break
    
    # check 
    if b > a:
        continue
    
    elif b == a:
        break
    
    else:
        ans = -1
        break     

print(ans)