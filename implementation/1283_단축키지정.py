### 1283 단축키 지정 (S1)
### 문자열, 구현

import sys
input = sys.stdin.readline

N = int(input())
words = []
ans = []
used = set()
for i in range(N):
    words.append(list(input().split()))
            
def sol(option):
    for i in range(len(option)):
        if option[i][0] not in used: # 첫글자 검사
            used.add(str.upper(option[i][0]))
            used.add(str.lower(option[i][0]))
            option[i] = '[' + option[i][0] + ']' + option[i][1:]
            return " ".join(option)

    else:
        for i in range(len(option)):
            for j in range(len(option[i])):
                if option[i][j] not in used:
                    used.add(str.upper(option[i][j]))
                    used.add(str.lower(option[i][j]))
                    option[i] = option[i][:j] + '[' + option[i][j] + ']' + option[i][j+1:]
                    return " ".join(option)
                
        return " ".join(option) # 아무 수정도 없을 때

for next in words:
    ans.append(sol(next))
    
for next in ans:
    print(next)