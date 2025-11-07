### 10942.팰린드롬? (G4)
### 구현, 재귀, DP?
import sys
input = sys.stdin.readline

def recursive(s, e):
    if D[s][e] != -1: # 이전에 이미 탐색했다면
        return D[s][e]
    if s >= e: # 똑같으면 반드시 팰린드롬
        D[s][e] = 1
        return D[s][e]
    if nums[s] != nums[e]: # 끝 숫자가 다르면 팰린드롬 아님
        D[s][e] = 0
        return D[s][e]
    
    ## 재귀해서 그 값 가져와서 리턴
    result = recursive(s+1, e-1)
    D[s][e] = result
    return result

N = int(input())
nums = list(map(int, input().split()))
D = [[-1 for _ in range(N)] for _ in range(N)]

Q = int(input())
for i in range(Q):
    s, e = map(int, input().split())
    print(recursive(s-1, e-1))