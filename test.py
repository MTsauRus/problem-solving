import sys
input = sys.stdin.readline

N = int(input())
foods = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')

# 1부터 2^N - 1 까지의 모든 부분집합을 확인
# 1 << N 은 2^N 과 동일합니다.
for i in range(1, 1 << N):
    S, B = 1, 0  # 신맛(곱), 쓴맛(합)

    # 0번 음식부터 N-1번 음식까지 확인
    for j in range(N):
        # i의 j번째 비트가 1이라면 j번째 음식을 사용한다는 의미
        if i & (1 << j):
            S *= foods[j][0]
            B += foods[j][1]

    ans = min(ans, abs(S - B))

print(ans)