import sys
input = sys.stdin.readline
A, K = map(int, input().split())

moloco = 0
others = 0
tmps = []
for _ in range(A):
    a, b = map(int, input().split())
    tmp = a-b
    if tmp>=0:
        moloco += 1
    else:
        others += 1
        tmps.append(-tmp)
tmps.sort()
if moloco >= K:
    print(0)
else:
    print(tmps[K-moloco-1])
    
    
    