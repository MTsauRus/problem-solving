### 5215.햄버거 다이어트 (D3)
T = int(input())
for t in range(1, T+1):
    N, cal_max = map(int, input().split())
    score, cal = [0], [0]
    for _ in range(N):
        a, b = map(int, input().split())
        score.append(a)
        cal.append(b)
    
    D = [[0 for _ in range(cal_max+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for w in range(1, cal_max+1):
            if cal[i] > w: 
                D[i][w] = D[i-1][w]
            else:
                D[i][w] = max(D[i-1][w], D[i-1][w-cal[i]] + score[i])
    
    print(f"#{t} {D[N][cal_max]}")