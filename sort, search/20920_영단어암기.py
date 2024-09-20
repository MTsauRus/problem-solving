import sys
input = sys.stdin.readline
a, b = map(int, input().split())
D = {}
L = []
for i in range(a):
    tmp = input().strip()
    if len(tmp) < b:
        continue
    if tmp not in D.keys():
        D[tmp] = [1, len(tmp)]
    else:
        D[tmp][0] += 1

for key, value in D.items():
    L.append([value, key])
    
L.sort(key= lambda x : (-x[0][0],-x[0][1], x[1]))
for next in L:
    print(next[1])

# 첫 제출
# a, b = map(int, input().split())
# D = {}
# L = []
# for i in range(a):
#     tmp = input().strip()
#     if tmp not in D.keys():
#         D[tmp] = [-1, -len(tmp)]
#     else:
#         D[tmp][0] -= 1
    
# for key, value in D.items():
#     L.append([value, key])

# L.sort()

# for next in L:
#     if next[0][1] <= -b:
#         print(next[1])