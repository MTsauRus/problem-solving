### N과 M (4) (S3)
import sys
input = sys.stdin.readline

lim, length = map(int, input().split())

def func(lim, length, curr, arr):
    if len(arr) == length:
        print(*arr)
        return
    
    for i in range(1, lim+1):
        if i < curr:
            continue
        func(lim, length, i, arr + [i])

used = [0] * (lim + 1)
func(lim, length, 1, [])