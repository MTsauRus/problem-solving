import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')
nums = [i for i in range(N)]

for x in range(K, N//2+1):
    for selected in combinations(nums, x):
        teams = [False for _ in range(N)]
        for next in selected:
            teams[next] = True
        
        teamA = []
        teamB = []
        for i in range(N):
            if teams[i]:
                teamA.append(i)
            else:
                teamB.append(i)
        
        tmpSumA = 0
        tmpSumB = 0
        for member in combinations(teamA, 2):
            s, e = member[0], member[1]
            tmpSumA += G[s][e]
            tmpSumA += G[e][s]
        
        for member in combinations(teamB, 2):
            s, e = member[0], member[1]
            tmpSumB += G[s][e]
            tmpSumB += G[e][s]
        
        
        ans = min(ans, abs(tmpSumA-tmpSumB))
print(ans)