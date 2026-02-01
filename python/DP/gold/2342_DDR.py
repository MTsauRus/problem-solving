### 2342. DDR (G3)
### DP
import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
nums.pop()

# D[k][i][j] : k번째까지 고려, 현재위치 i, j
D = [[[400000 for _ in range(5)] for _ in range(5)] for _ in range(len(nums)+1)]
F = [[1, 2, 2, 2, 2], 
     [0, 1, 3, 4, 3],
     [0, 3, 1, 3, 4],
     [0, 4, 3, 1, 3],
     [0, 3, 4, 3, 1]]

D[0][0][0] = 0
D[0][nums[0]][0] = 2
D[0][0][nums[0]] = 2 # 처음 경우의 수는 왼발, 오른발을 각각 nums[0]에 두는 방법밖에 없음

for k in range(len(nums)):
    for i in range(5):
        for j in range(5):
            # i가 움직이는 경우: 이전 칸 + 다음 움직였을 때의 힘의 합
            D[k+1][nums[k]][j] = min(D[k+1][nums[k]][j], D[k][i][j] + F[i][nums[k]])
            # j가 움직이는 경우
            D[k+1][i][nums[k]] = min(D[k+1][i][nums[k]], D[k][i][j] + F[j][nums[k]]) 
            
ans = 400001
for i in range(5):
    for j in range(5):
        if ans > D[len(nums)][i][j]:
            ans = D[len(nums)][i][j]

print(ans)