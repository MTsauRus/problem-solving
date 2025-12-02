### 1215. 회문1 (D3)
### 브루트 포스

def is_palindrom(l):
    n = len(l)
    if n%2 == 0: # 짝수
        left = l[0:n//2]
        right = l[n//2:]
    else: # 홀수
        left = l[0:n//2]
        right = l[n//2+1:]

    right_rev = "".join(right[i] for i in range(len(right)-1, -1, -1))
    
    if left == right_rev:
        return True
    else:
        return False
        
T = 10
for t in range(1, T+1):
    N = int(input())
    if N == 1:
        print(64)
        continue
    elif N > 8:
        print(0)
        continue
    
    G = []
    G_rev = ["" for _ in range(8)]
    for i in range(8):
        G.append(input().strip())
    for i in range(8):
        for j in range(8):
            G_rev[i] += G[j][i]
    
    ans = 0
    for i in range(8):
        next1 = G[i]
        next2 = G_rev[i]
        for j in range(0, 8-N+1):
            if is_palindrom(next1[j:j+N]):
                ans += 1
            if is_palindrom(next2[j:j+N]):
                ans += 1
    
    print(f'#{t} {ans}')