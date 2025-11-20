### 1208. flatten

for T in range(1, 11):
    ans = -10
    N = int(input())
    ground = list(map(int, input().split()))
    height = [0 for _ in range(101)]
    
    for h in ground:
        height[h] += 1
        
    h_max = max(ground)
    h_min = min(ground)
    front = h_min
    rear = h_max
    
    for i in range(N):
        height[h_max] -= 1
        height[h_min] -= 1
        height[h_max-1] += 1
        height[h_min+1] += 1
        if height[h_max] == 0:
            h_max -= 1
        if height[h_min] == 0:
            h_min += 1
        
        if h_max - h_min == 1:
            ans = 1
            break
        elif h_max == h_min:
            ans = 0
            break
        
    if ans == 1 or ans == 0:
        print(f'#{T} {ans}')
    else:
        print(f'#{T} {h_max-h_min}')