### N과 M (9) (S2)
### 백트래킹
import sys
input = sys.stdin.readline

lim, length = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []
def func(lim, length, used, ch):
    if ch.count(" ") == length:
        ans.append(ch)
        return
    
    for i in range(lim):
        if not used[i]:
            used[i] = True
            func(lim, length, used, ch + str(nums[i]) + " ")
            used[i] = False
    
used = [0] * lim
func(lim, length, used, "")

#ans = sorted(list(set(ans)))
#ans = sorted(set(ans), key=lambda x: list(map(int, x.split())))
ans = sorted(set(ans), key = lambda x : list(map(int, x.split())))

for next in ans:
    print(next.strip())