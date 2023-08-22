import sys
input = sys.stdin.readline

global swaps
swaps = 0

def msort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = msort(arr[:mid])
    right = msort(arr[mid:])
    return merge(right, left)

def merge(right, left):
    global swaps
    merged = []
    r = l = 0
    
    while r < len(right) and l < len(left):
        if right[r] < left[l]:
            merged.append(right[r])
            cnt = len(left) - l
            swaps += cnt
            r += 1
        else:
            merged.append(left[l])
            l += 1

        

    merged += right[r:]
    merged += left[l:]

    return merged


N = int(input())
A = [int(a) for a in input().split()]

msort(A)

print(swaps)