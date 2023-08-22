import sys
input = sys.stdin.readline

N = int(input())
D = {}
for i in range(N):
    x = input().rstrip()
    try:
        D[len(x)].add(x)
    except:
        D[len(x)] = {x}
L = list(D.keys())
print(L)
print(D)
L.sort()
for i in L:
    D[i] = list(D[i])
    D[i].sort()
for i in range(len(L)):
    for j in D[L[i]]:
        print(j)