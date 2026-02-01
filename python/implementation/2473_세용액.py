### 2473. 세 용액 (G3)
### 투 포인터
import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split()))) # nlogn
ans_list = []
ans_flag = 10**9 * 3 + 1

for i in range(0, N-2):
    s, e = i+1, N-1
    while s<e:
        tmp_sum = nums[i]+nums[s]+nums[e]
        if tmp_sum == 0:
            ans_list = [nums[i], nums[s], nums[e]]
            print(*ans_list)
            exit(0)
        if abs(tmp_sum) < ans_flag: # 0은 아닌데 최소값이면 저장
            ans_list = [nums[i], nums[s], nums[e]]
            ans_flag = abs(tmp_sum)
        if tmp_sum > 0: # 0보다 크면 더하는 수를 줄임
            e -= 1
        else:
            s += 1
print(*ans_list)