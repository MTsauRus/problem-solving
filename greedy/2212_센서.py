### 2212. 센서 (G5)
### 그리디
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M >= N:
    print(0)
    exit(0)
nums = list(map(int, input().split()))
nums.sort()
ans = nums[-1]-nums[0]

gap = []
for i in range(0, len(nums)-1):
    gap.append(nums[i+1]-nums[i])
    
gap.sort(key=lambda x:-x)

for i in range(M-1):
    ans -= gap[i]

print(ans)