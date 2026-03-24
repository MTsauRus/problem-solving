### 5676. 음주코딩 (G1)
### 세그트리
import sys
input = sys.stdin.readline

while True:
    next = input()
    if next == "": break
    N, K = map(int, next.split())
    arr = [0] + list(map(int, input().split()))
    T = [0] * (4*N)

    def init(node, cs, ce):
        if cs == ce:
            T[node] = arr[cs]
            return
        
        mid = (cs + ce) // 2
        init(node*2, cs, mid)
        init(node*2+1, mid+1, ce)
        T[node] = T[node*2]*T[node*2+1]
        
    def update(node, cs, ce, idx, val):
        if idx < cs or idx > ce: return
        if cs == ce:
            T[node] = val
            arr[idx] = val
            return
        
        mid = (cs + ce) // 2
        update(node*2, cs, mid, idx, val)
        update(node*2+1, mid+1, ce, idx, val)
        T[node] = T[node*2]*T[node*2+1]
        
    def query(node, cs, ce, gs, ge):
        if ce < gs or ge < cs: return 1
        if gs <= cs and ce <= ge: return T[node]
        mid = (cs + ce) // 2
        lres = query(node*2, cs, mid, gs, ge)
        rres = query(node*2+1, mid+1, ce, gs, ge)
        
        return lres*rres

    for _ in range(K):
        q, a, b = map(str, input().split())
        a = int(a)
        b = int(b)
        ans = ""
        if q == 'C':
            update(1, 1, N, a, b)
        else:
            tmp = query(1, 1, N, a, b)
            if tmp == 0:
                ans+=("0")
            elif tmp>0:
                ans+=("+")
            else:
                ans+=("-")
            
        print(ans)