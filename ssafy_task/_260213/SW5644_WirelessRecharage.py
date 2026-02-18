T = int(input())

dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]

for t in range(1, T+1):
    M, A = map(int, input().split())
    A_dir = list(map(int, input().split()))
    B_dir = list(map(int, input().split()))
    
    charger = []
    for _ in range(A):
        charger.append(list(map(int, input().split())))
        
    ar, ac = 1, 1
    br, bc = 10, 10
    
    ans = 0
    
    for i in range(M+1):
        A_charger = []
        B_charger = []
        A_max = 0
        B_max = 0
        # 접속체크
        for j in range(A):
            next = charger[j]
            # A 체크
            if (abs(next[0]-ac) + abs(next[1]-ar)) <= next[2]:
                A_charger.append([j, next[3]])
                A_max = max(A_max, next[3])
            # B 체크
            if (abs(next[0]-bc) + abs(next[1]-br)) <= next[2]:
                B_charger.append([j, next[3]])
                B_max = max(B_max, next[3])
                
        # 최댓값계산
        localMax = 0
        if len(A_charger) == 0 and len(B_charger) != 0:
            localMax = B_max
        elif len(A_charger) != 0 and len(B_charger) == 0:
            localMax = A_max
        elif len(A_charger) != 0 and len(B_charger) != 0:
            for a in range(len(A_charger)):
                for b in range(len(B_charger)):
                    tmpSum = 0
                    # 같은 charger라면 반띵 후 합산-> 그냥 A charger의 값.
                    if A_charger[a][0] == B_charger[b][0]:
                        tmpSum = A_charger[a][1]
                    else:
                        tmpSum += A_charger[a][1]
                        tmpSum += B_charger[b][1]
                    localMax = max(localMax, tmpSum)
        
        # print(f"t: {i}, localMax: {localMax}")
        # print(f"A: [{ar}, {ac}] {A_charger}, B: [{br}, {bc}] {B_charger}")
        ans += localMax
        
        # 다음칸이동
        if i < M:
            ar += dr[A_dir[i]]
            ac += dc[A_dir[i]]
            br += dr[B_dir[i]]
            bc += dc[B_dir[i]]
    
    print(f"#{t} {ans}")