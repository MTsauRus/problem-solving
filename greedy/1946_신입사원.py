### 1946. 신입사원 (S1)
### 그리디 알고리즘
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    nums = []
    for n in range(N):
        nums.append(list(map(int, input().split())))
        
    numA = sorted(nums)
    numB = sorted(nums, key=lambda x:x[1])
    
    ans = 1
    Bmax = numA[0][1]
    
    for i in range(1, N):
        if numA[i][1] < Bmax:
            ans += 1
            Bmax = numA[i][1]
    
    print(ans)