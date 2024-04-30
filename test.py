while True:
    a=list(map(list, (input().split())))
    if a[0][0]+a[0][1]+a[0][2] == "END":
        break
    a.reverse()
    for i in range(len(a)):
        a[i].reverse()
        for j in range(len(a[i])):
            print(a[i][j], end="")
        print(" ", end="")
    print("")