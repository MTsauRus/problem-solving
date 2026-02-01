### 아리스, 청소합니다! (Easy) (G2)
### 구현
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
R, C, D = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(H)] # rule
B = [list(map(int, input().strip())) for _ in range(H)]
cleaned = [[False] * W for _ in range(H)]
ans = 0
tmp = 0 # 임시이동거리
limit = H*W*4

next = [R, C, D]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    r, c, d = next
    if not (0 <= r < H) or not (0 <= c < W): # 유효성 검사
        break

    
    if not cleaned[r][c]:
        cleaned[r][c] = True
        d = (d + A[r][c]) % 4 # A rule 방향 조정
        r = r + dr[d]
        c = c + dc[d]
        next = [r, c, d] # 다음 칸
        tmp += 1
        ans += tmp
        tmp = 0
    
    else: # 이미 청소가 되어있었다면
        d = (d + B[r][c]) % 4 # B rule 방향 조정
        r = r + dr[d]
        c = c + dc[d] 
        next = [r, c, d] # 다음칸
        tmp += 1
        if tmp > limit: # 최대 허용 크기 사이클
            break
    
print(ans)