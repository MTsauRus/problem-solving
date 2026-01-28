### 1,2,3 더하기 (S3)
import sys
input = sys.stdin.readline

N = int(input())
D = [0]*11
D[0] = 0
D[1] = 1
D[2] = 2
D[3] = 4
for i in range(4, 11):
    D[i] = D[i-1]+D[i-2]+D[i-3]
for i in range(N):
    num = int(input())
    print(D[num])
    