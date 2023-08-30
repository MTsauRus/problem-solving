### 마인크래프트 (S2)
import sys
input = sys.stdin.readline

row, col, inventory = map(int, input().split())
ground = []
for r in range(row):
    ground.append(list(map(int, input().split()))) 

max_height = max(max(ground))
ans = (64000000, 0)
for level in range(max_height+1):
    time = 0
    box = inventory
    for r in range(row):
        for c in range(col):
            now = ground[r][c] - level
            if now > 0:
                box += now
                time += 2 * now
            
            elif now < 0:
                box += now
                time += -1 * now
                
    if box < 0:
        continue
    else:
        if time <= ans[0]:
            ans = (time, level)
            
print(*ans)
                