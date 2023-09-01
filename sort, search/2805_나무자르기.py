### 나무 자르기 (S2)
import sys
input = sys.stdin.readline

N, need = map(int, input().split())
T = list(map(int, input().split()))
T.sort(reverse=True)

start = 0
end = T[0]
cnt = 0

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for tree in T:
        if tree - mid < 0:
            break
        else:
            cnt += tree - mid

    if cnt >= need:
        start = mid + 1

    else:
        end = mid - 1

print(end)