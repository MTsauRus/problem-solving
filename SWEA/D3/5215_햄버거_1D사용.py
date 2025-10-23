### 5215.햄버거 다이어트 (D3)
T = int(input())
for t in range(1, T+1):
    N, cal_max = map(int, input().split())
    score, cal = [0], [0]
    for _ in range(N):
        a, b = map(int, input().split())
        score.append(a)
        cal.append(b)
    
    D = [0 for _ in range(cal_max+1)]
    for i in range(1, N+1, 1):
        for w in range(cal_max, cal[i]-1, -1):
            D[w] = max(D[w], D[w-cal[i]] + score[i])            
    print(f"#{t} {D[cal_max]}")