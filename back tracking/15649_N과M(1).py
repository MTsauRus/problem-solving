### N과 M (1) (S3)
### 백트래킹
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
l = [i for i in range(N+1)]
def solve(N, M):
    ans = []
    for i in range(1, N+1):
        
        