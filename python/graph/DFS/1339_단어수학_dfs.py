### 1339. 단어 수학 (G4)
### DFS
import sys
input = sys.stdin.readline

N = int(input())
voca = []
ch_set = set()

for _ in range(N):
    next = list(input().strip())
    voca.append(next)
    for ch in next:
        ch_set.add(ch)
        
ch_list = list(ch_set)
visited = [False for _ in range(10)]
ans = 0
ch_weight = [0 for _ in range(len(ch_list))]
for next in voca:
    mult = 1
    for i in range(len(next)-1, -1, -1):
        ch_weight[ch_list.index(next[i])] += mult
        mult *= 10
    

def ch_sort(depth, tot):
    global ans
    
    if depth == len(ch_list):
        ans = max(ans, tot)
        return
    
    for i in range(9, 9-len(ch_list), -1):
        if not visited[i]:
            visited[i] = True
            ch_sort(depth + 1, tot + (ch_weight[depth]) * i)
            visited[i] = False

ch_sort(0, 0)
print(ans)