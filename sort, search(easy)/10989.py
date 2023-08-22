import sys
input = sys.stdin.readline

N = int(input())

cnt = [0 for x in range(10001)]

for _ in range(N):
    cnt[int(input())] += 1

#print("___________-")
for i in range(len(cnt)):
    while cnt[i] > 0:
        print(i)
        cnt[i] -= 1


    
