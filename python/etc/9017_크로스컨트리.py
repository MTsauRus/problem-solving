### 크로스 컨트리 (S3)
### 구현

import sys
n = int(input())
for i in range(n):
    a = int(input())
    l = list(map(int, input().split()))
    cnt = {}
    
    for j in range(a):
        if l[j] not in cnt.keys():
            cnt[l[j]] = 1
        else:
            cnt[l[j]] += 1
            
    dq = [] # 실격 팀
    for key, value in cnt.items():
        if value < 6:
            dq.append(key)
    
    k = 0
    while k < a: 
        if l[k] in dq:
            l.pop(k)
            a-=1
            continue
        k+=1
    
    score = {}
    fifth = []
    for w in range(a):
        if l[w] not in score.keys():
            score[l[w]] = [1, w+1] # (순위, 점수)
        else:
            score[l[w]][0] += 1 # 순위 + 1
            
            if score[l[w]][0] <= 4: # 4등 이하만 점수 반영
                score[l[w]][1] += w+1 # 점수
                
            if score[l[w]][0] == 5: # 5등 순위 따로 저장
                fifth.append(l[w])
                continue
    
    min = sys.maxsize
    winner = []
    for key, value in score.items():
        if value[1] < min:
            min = value[1]
            winner.clear()
            winner.append(key)
        elif value[1] == min:
            winner.append(key)
    
    if len(winner) == 1:
        print(winner[0])
    else:
        for i in fifth:
            if i in winner:
                print(i)
                break