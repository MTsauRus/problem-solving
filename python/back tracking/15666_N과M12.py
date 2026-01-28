### N과 M (12) (S2)
### 백트래킹

import sys
input = sys.stdin.readline

lim, length = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
ans_set = []

def func(lim, ptr, ans):
    if ans.count(" ") == length:
        ans_set.append(ans)
        return
    
    for i in range(ptr, len(nums)):
        func(lim, i, ans + str(nums[i]) + " ")

func(lim, 0, "")

sorted(ans_set, key = lambda x: list(map(int, x.split())))

for next in ans_set:
    print(next)