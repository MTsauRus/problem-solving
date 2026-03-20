### 1013. Contact (G5)
### 문자열, 구현

## 다시풀어~


import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    next = input().strip()
    
    next += "2"
    idx = 0
    goal = len(next) - 1
    
    
    while idx < goal:
        if next[idx] == '0':
            # 0이 오면 다음은 반드시 1이 와야 함. 
            if next[idx+1] == '1':
                idx += 2
                continue
            # 그 외인 경우 break
            elif next[idx+1] == '0' or next[idx+1] == '2':
                break
        # 시작이 1이면
        elif next[idx] == '1':
            tmpIdx = 1
            # 뒤에 반드시 00이 와야 함
            if next[idx+tmpIdx] != '0':
                break
            tmpIdx += 1
            if next[idx+tmpIdx] != '0':
                break
            tmpIdx += 1
            
            # 0 계속 붙이기
            while next[idx+tmpIdx] == '0':
                tmpIdx += 1
                
            # 만약 0 뒤에 1이 아예 안왔다면 실패
            if next[idx+tmpIdx] == '2':
                break
            tmpIdx += 1
            
            while next[idx+tmpIdx] == '1':
                tmpIdx += 1
            
            if next[idx+tmpIdx] == '2':
                idx = goal
                break
            else:
                if next[idx+tmpIdx] == '0' and next[idx+tmpIdx+1] == '0':
                    idx += tmpIdx-1
                    continue
                else:
                    idx += tmpIdx
                    continue
            
        else:
            idx = goal
            break
        
            
    
    if idx == goal:
        print("YES")
    else: print("NO")