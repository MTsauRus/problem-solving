### 소트 (G5)
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
S = int(input())

change = S
for i in range(N - 1):
    if change == 0:
        break
    max_now = arr[i]
    max_idx = i
    for j in range(i + 1, min(N, i + 1 + change)):
        if arr[j] > max_now:
            max_now = arr[j]
            max_idx = j
    
    for k in range(max_idx, i, -1):
        arr[k] = arr[k-1]
    arr[i] = max_now
    change -= (max_idx - i)
    
print(*arr)