### 한국이 그리울 땐 서버에 접속하지 (S3)
import sys
input = sys.stdin.readline
N = int(input())
p = input().strip()
p = list(p.split("*"))
front_len = len(p[0])
back_len = len(p[1])
for i in range(N):
    tmp = input().strip()
    if tmp[:front_len] == p[0] and tmp[len(tmp)-back_len:] == p[1] and front_len+back_len <= len(tmp):
        print("DA")
    else:
        print("NE")