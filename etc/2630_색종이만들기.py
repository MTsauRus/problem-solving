### 색종이 만들기 (S2)
### 재귀, 분할정복
import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
blue = 0
white =0

def func(x, y, n):
    global blue, white
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                func(x, y, n//2)
                func(x + n//2, y, n//2)
                func(x, y + n//2, n//2)
                func(x + n//2, y + n//2, n//2)
                return
    if color:
        blue += 1
    else:
        white += 1

func(0, 0, n)
print(white)
print(blue)
        