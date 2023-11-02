### 소트 (G5)
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr_rev = deque(sorted(arr, reverse=True))
S = int(input())
tmp = []

cnt = 0

while True:
    if S > N:
        if not arr_rev:
            break
        now_max = arr_rev.popleft()
        idx = arr.index(now_max)
        for i in range(idx, 0, -1):
            if arr[i-1] < arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
        S -= idx
        cnt += 1
    else:
        now_max = arr_rev[-(S+1)]
        idx = arr.index(now_max)
        if S < idx-cnt:
            for i in range(S):
                for j in range(N-1):
                    if arr[j] < arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                        break
        else:
            for i in range(idx, cnt, -1):
                if arr[i-1] < arr[i]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
        break
    
print(*arr)
