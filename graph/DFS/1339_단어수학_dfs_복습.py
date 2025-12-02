### 1339_단어 수학 (G4)
### dfs 방식 복습
import sys
input = sys.stdin.readline

# 입력
N = int(input())
words = []
ch_set = set()
for _ in range(N):
    word = list(input().strip())
    words.append(word)
    for ch in word:
        ch_set.add(ch)

# 가중치 선계산    
ch_list = list(ch_set)
ch_weight = [0 for _ in range(len(ch_list))]
for word in words:
    mult = 1
    for i in range(len(word)-1, -1, -1):
        ch_weight[ch_list.index(word[i])] += mult
        mult *= 10
        
ans = 0
visited = [False for _ in range(10)] # 9~0 숫자 사용 여부

def dfs(depth, tot):
    global ans
    if depth == len(ch_list):
        ans = max(ans, tot)
        return
    
    for i in range(9, 9 - len(ch_list), -1):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, tot + (i * ch_weight[depth]))
            visited[i] = False

dfs(0, 0)
print(ans)