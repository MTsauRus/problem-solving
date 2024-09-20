"""
1로 만들기 (S3)
DP
top down 방식
"""
import sys
input = sys.stdin.readline

a = int(input())
inf = 999999
D = [inf for i in range(3*a+1)]
D[a] = 0
for i in range(a-1, 0, -1):
    D[i] = min(D[i+1], D[i*2], D[i*3])+1
print(D[1])
    
    