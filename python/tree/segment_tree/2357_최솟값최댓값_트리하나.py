### 2357. 최솟값과 최댓값 (G1)
### 세그트리
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
    
T = [0 for _ in range(4*N)]

def init(idx, cs, ce):
    if cs == ce:
        # (min, max)
        T[idx] = (arr[cs], arr[cs])
    else:
        mid = (cs+ce)//2
        init(idx*2, cs, mid)
        init(idx*2+1, mid+1, ce)
        T[idx] = (min(T[idx*2][0], T[idx*2+1][0]), max(T[idx*2][1], T[idx*2+1][1]))

def query(idx, cs, ce, gs, ge):
    if ce < gs or ge < cs:
        return (float('inf'), -float('inf'))
    if gs <= cs and ce <= ge:
        return T[idx]
    mid=(cs+ce)//2
    lres = query(idx*2, cs, mid, gs, ge)
    rres = query(idx*2+1, mid+1, ce, gs, ge)
    return (min(lres[0], rres[0]), max(lres[1], rres[1]))

init(1, 1, N)

for _ in range(M):
    a, b = map(int, input().split())
    ans = query(1, 1, N, a, b)
    print(ans)