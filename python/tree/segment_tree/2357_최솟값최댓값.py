### 2357. 최솟값과 최댓값 (G1)
### 세그트리
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0]
for _ in range(N):
    arr.append(int(input()))

T_max = [0] * (4*N)
T_min = [0] * (4*N)

def init_max(idx, cs, ce):
    if cs == ce: # 리프
        T_max[idx] = arr[cs]    
    else:
        mid = (cs+ce)//2
        init_max(idx*2, cs, mid)
        init_max(idx*2+1, mid+1, ce)
        T_max[idx] = max(T_max[idx*2], T_max[idx*2+1])

def query_max(idx, cs, ce, gs, ge):
    if ce < gs or ge < cs:
        return -float('inf')
    if gs <= cs and ce <= ge:
        return T_max[idx]

    mid = (cs+ce)//2
    lmax = query_max(idx*2, cs, mid, gs, ge)
    rmax = query_max(idx*2+1, mid+1, ce, gs, ge)
    return max(lmax, rmax)

def init_min(idx, cs, ce):
    if cs == ce: # 리프
        T_min[idx] = arr[cs]    
    else:
        mid = (cs+ce)//2
        init_min(idx*2, cs, mid)
        init_min(idx*2+1, mid+1, ce)
        T_min[idx] = min(T_min[idx*2], T_min[idx*2+1])


def query_min(idx, cs, ce, gs, ge):
    if ce < gs or ge < cs:
        return float('inf')
    if gs <= cs and ce <= ge:
        return T_min[idx]

    mid = (cs+ce)//2
    lmin = query_min(idx*2, cs, mid, gs, ge)
    rmin = query_min(idx*2+1, mid+1, ce, gs, ge)
    return min(lmin, rmin)

init_max(1, 1, N)
init_min(1, 1, N)

for _ in range(M):
    a, b = map(int, input().split())
    print(query_min(1, 1, N, a, b), end=" ")
    print(query_max(1, 1, N, a, b))
