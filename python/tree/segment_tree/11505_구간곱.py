### 11505. 구간 곱 구하기 (G1)
### 세그트리

import sys
input = sys.stdin.readline
MOD = 1000000007
# M: 변경, K: 구간곱 수
N, M, K = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]

T = [0] * (N*4)

def init(node, cs, ce):
    if cs == ce:
        T[node] = arr[cs]
        return
    else:
        mid = (cs+ce)//2
        init(node*2, cs, mid)
        init(node*2+1, mid+1, ce)
        T[node]=(T[node*2]*T[node*2+1])%MOD
        return

def update(node, cs, ce, idx, val):
    # 범위 벗어나면 컷
    if idx < cs or idx > ce: return
    
    if cs == ce:
        arr[idx] = val
        T[node] = val
        return
    
    mid = (cs + ce) // 2
    update(node*2, cs, mid, idx, val)
    update(node*2+1, mid+1, ce, idx, val)
    T[node] = (T[node*2] * T[node*2+1])%MOD
    
    
    
def query(node, cs, ce, gs, ge):
    if ce < gs or ge < cs:
        return 1
    
    if gs <= cs and ce <= ge:
        return T[node]
    
    mid = (cs+ce)//2
    lres = query(node*2, cs, mid, gs, ge)
    rres = query(node*2+1, mid+1, ce, gs, ge)
    return ((lres%MOD)*(rres%MOD))%MOD
    
init(1, 1, N)
for _ in range(M+K):
    q, a, b = map(int, input().split())
    if q == 1:
        update(1, 1, N, a, b)
    else:
        print(query(1, 1, N, a, b))
        