### 1289. 메모리 복구
### 구현, S5~4?
T = int(input())
for t in range(1, T+1):
    l = list(map(int, input().strip()))
    flag = 1
    ans = 0
    for i in range(len(l)):
        if flag == l[i]:
            ans += 1
            if flag == 1:
                flag = 0
            else:
                flag = 1
    
    print(f'#{t} {ans}')