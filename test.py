a=int(input())
b = list(input().strip())
for i in range(a-1):
    tmp = list(input().strip())
    for j in range(len(b)):
        if b[j] != tmp[j]:
            b[j] = '?'

for n in b:
    print(n, end="")