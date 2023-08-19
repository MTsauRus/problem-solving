### 물통 (G5)
import sys
input = sys.stdin.readline

capacity = list(map(int, input().split())) # [A, B, C]
#A = 0, B = 1, C = 2
move = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
# check visited for (a, b), becuase c can be calculated by (total - a - b)
visited = [[False for _ in range(201)] for _ in range(201)]
ans = []
start = [0, 0, capacity[2]] # init: [0, 0, c]

def bfs(start:list): # start = [0, 0, 10]
    queue = []
    queue.append(start)
    visited[start[0]][start[1]] = True
    while queue:
        now = queue.pop(0) # now = [0, 0, 10]
        if now[0] == 0:
            ans.append(now)

        for m in move:
            bucket = now[:] # 얕은 복사
            if bucket[m[0]] > capacity[m[1]] - bucket[m[1]]: # 넘치는 경우
                rest = capacity[m[1]] - bucket[m[1]]
                bucket[m[1]] = capacity[m[1]]
                bucket[m[0]] -= rest
            
            else: # 넘치지 않는 경우
                bucket[m[1]] += bucket[m[0]]
                bucket[m[0]] = 0

            if not visited[bucket[0]][bucket[1]]:
                visited[bucket[0]][bucket[1]] = True
                queue.append(bucket)


bfs(start)
ans.sort(key=lambda x : x[2])
for a in ans:
    print(a[2], end=" ")
             


