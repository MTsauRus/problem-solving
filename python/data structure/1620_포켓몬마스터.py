### 나는야 포켓몬 마스터 이다솜 (S4)
import sys
input = sys.stdin.readline

D = dict()
E = dict()
N, Q = map(int, input().split())
for i in range(1, N+1):
    D[i] = input().strip()
    E[D[i]] = i
for i in range(Q):
    req = input().strip()
    try:
        print(E[req])
    except:
        print(D[int(req)])
