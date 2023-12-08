a=int(input())
tmp=1
for i in range(a-1, 0, -1):
    for j in range(0, i, 1):
        print(" ",end="")
    for k in range(0, tmp, 1):
        print("*",end="")
    print("")
    tmp+=2
for i in range(0, 2*a-1, 1):
    print("*",end="")
print("")
tmp-=2
for i in range(1, a, 1):
    for j in range(0, i, 1):
        print(" ", end="")
    for k in range(tmp, 0, -1):
        print("*", end="")
    print("")
    tmp-=2