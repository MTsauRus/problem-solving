### N과 M (1) (S3)
### 백트래킹
import sys
input = sys.stdin.readline

lim, length = map(int, input().split())

def func(lim, length, arr, used):
    if len(arr) == length:
        print(*arr)
        return
    
    for i in range(1, lim+1):
        if not used[i]:
            used[i] = True
            func(lim, length, arr + [i], used)
            used[i] = False
        
used = [False for i in range(lim+1)]    
func(lim, length, [], used)