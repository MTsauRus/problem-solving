### N과 M (5) (S3)
### 백트래킹

import sys
input = sys.stdin.readline

lim, length = map(int, input().split())
num = sorted(list(map(int, input().split())))

def func(lim, length, ptr, used, arr):
    if len(arr) == length:
        print(*arr)
        return
    
    for i in range(ptr, lim):
        if not used[i]:
            used[i] = True
            func(lim, length, ptr, used, arr + [num[i]])
            used[i] = False
            
used = [0] * lim
func(lim, length, 0, used, [])