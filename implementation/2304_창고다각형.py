### 2304 창고 다각형
### 구현
import sys
input = sys.stdin.readline

N = int(input())
blocks = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x : (x[1], x[0]))
high = blocks.pop()
ans = high[1]
front = high[0]
back = high[0] + 1
while blocks:
    next = blocks.pop()
    if front <= next[0] < back:
        continue
    elif next[0] < front:
        ans += (front-next[0])*next[1]
        front = next[0]
    else:
        ans += ((next[0]+1)-back)*next[1]
        back = next[0]+1
print(ans)