### 1244.최대 상금 (D3)
from collections import deque
T = int(input())

def bfs(num, max_iter): # num: str
    queue = deque([(num, 0)])
    visited = set()
    len_num = len(num)
    ans_list = []
    
    while queue:
        now = queue.popleft()
        now_num, now_iter = now[0], now[1]
        if now_iter == max_iter + 1:
            return max(ans_list)
        now_list = list(now_num)
        for i in range(0, len_num-1, 1):
            for j in range(i+1, len_num, 1):
                tmp_list = now_list[:]
                tmp_list[i], tmp_list[j] = tmp_list[j], tmp_list[i]
                tmp_num = "".join(map(str, tmp_list))
                if (tmp_num, now_iter + 1) not in visited:
                    visited.add((tmp_num, now_iter + 1))
                    queue.append((tmp_num, now_iter + 1))
                    if now_iter+1 == max_iter:
                        ans_list.append(int(tmp_num))
    return max(ans_list)

ans = []
    
for t in range(1, T+1):
    num, iter = input().split()
    iter = int(iter)
    ans.append(bfs(num, iter))
    
for i in range(len(ans)):
    print(f"#{i+1} {ans[i]}")