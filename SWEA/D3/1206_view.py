### 1206. view (D3)
T = 10
for i in range(1, T+1):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for j in range(2, n-2, 1):
        tmp_max = max(l[j-2], l[j-1], l[j+1], l[j+2])
        if l[j] <= tmp_max:
            continue
        ans += l[j] - tmp_max
    print(f'#{i} {ans}')
