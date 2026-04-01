### 3079. 입국심사 (G5)
### 파라메트릭 서치
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

def calc(limit, times):
    return sum(limit//x for x in times)

s, e = 0, 1000000000 * 1000000000

while s < e:
    mid = (s+e) // 2
    
    if calc(mid, times) >= M:
        e = mid
    
    elif calc(mid, times) < M:
        s = mid+1
    

print(e)