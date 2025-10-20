### 17404. RGB거리 2 (G4)
### DP
import sys
input = sys.stdin.readline
n = int(input())
costs = []    
for i in range(n):
    costs.append(list(map(int, input().split())))


DR = [[costs[0][0], float('inf'), float('inf')]] + [[0, 0, 0] for _ in range(n-1)]
DG = [[float('inf'), costs[0][1], float('inf')]] + [[0, 0, 0] for _ in range(n-1)]
DB = [[float('inf'), float('inf'), costs[0][2]]] + [[0, 0, 0] for _ in range(n-1)]

for i in range(1, n-1):
    for j in range(3):
        DR[i][j] = min(DR[i-1][(j+1)%3], DR[i-1][(j-1)%3]) + costs[i][j]
        DG[i][j] = min(DG[i-1][(j+1)%3], DG[i-1][(j-1)%3]) + costs[i][j]
        DB[i][j] = min(DB[i-1][(j+1)%3], DB[i-1][(j-1)%3]) + costs[i][j]

DR[n-1][1] = min(DR[n-2][0], DR[n-2][2]) + costs[n-1][1]
DR[n-1][2] = min(DR[n-2][0], DR[n-2][1]) + costs[n-1][2]
DG[n-1][0] = min(DG[n-2][1], DG[n-2][2]) + costs[n-1][0]
DG[n-1][2] = min(DG[n-2][0], DG[n-2][1]) + costs[n-1][2]
DB[n-1][0] = min(DB[n-2][1], DB[n-2][2]) + costs[n-1][0]
DB[n-1][1] = min(DB[n-2][0], DB[n-2][2]) + costs[n-1][1]

print(min(DR[n-1][1], DR[n-1][2], DG[n-1][0], DG[n-1][2], DB[n-1][1], DB[n-1][0]))