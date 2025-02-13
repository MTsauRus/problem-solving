### N과 M (2) (S3)
### 백트래킹
import sys
input = sys.stdin.readline

lim, length = map(int, input().split())

def func(lim, length, start, arr):
    if len(arr) == length:
        print(*arr)
        return
    
    for i in range(start, lim+1):
        func(lim, length, i+1, arr + [i])

func(lim, length, 1, [])