### 1339. 단어 수학 (G4)
### 그리디
import sys
input = sys.stdin.readline

N = int(input())
words = []
ch_set = set()
for _ in range(N):
    word = list(input().strip())
    words.append(word)
    for ch in word:
        ch_set.add(ch)
        
ch_list = list(ch_set)
ch_weight = [0 for _ in range(len(ch_list))]

for word in words:
    mult = 1
    for i in range(len(word)-1, -1, -1):
        ch_weight[ch_list.index(word[i])] += mult
        mult *= 10
        
ch_weight.sort(key = lambda x : -x)

ans = 0
for i, w in enumerate(ch_weight):
    ans += w * (9 - i)
print(ans)