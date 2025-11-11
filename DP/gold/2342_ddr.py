### 2342. DDR (G3)
### DP
import sys
input = sys.stdin.readline

arr = [0] + list(map(int, input().split()))
arr.pop()

# D[k][i][j]: 현재 발 i, j이고 k번 까지 고려했을 때의 최소점수
D = [[[400000 for _ in range(5)] for _ in range(5)] for _ in range(len(arr)+10)]

# force[s][e] : s -> e 일 때 드는 힘
force = [[0, 2, 2, 2, 2], 
         [0, 1, 3, 4, 3], 
         [0, 3, 1, 3 ,4], 
         [0, 4, 3, 1, 3], 
         [0, 3, 4, 3, 1]]

D[1][0][0] = 0
D[1][arr[1]][0] = 2
D[1][0][arr[1]] = 2
for k in range(2, len(arr)):
    for i in range(5):
        for j in range(5):
            D[k][i][arr[k]] = min(D[k][i][arr[k]], D[k-1][i][j] + force[j][arr[k]])
            D[k][arr[k]][j] = min(D[k][arr[k]][j], D[k-1][i][j] + force[i][arr[k]])

ans = 4000000
for i in range(5):
    for j in range(5):
        if ans > D[len(arr)-1][i][j]:
            ans = D[len(arr)-1][i][j]

print(ans)
print(D)