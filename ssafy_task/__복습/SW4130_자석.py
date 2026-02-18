T = int(input())

def rotate_right(mgNum, CW):
    global magnet,mgPtr,isRotate    
    if mgNum == 3:
        return
    now = magnet[mgNum]
    next = magnet[mgNum+1]
    if now[(mgPtr[mgNum]+2)%8] != next[(mgPtr[mgNum+1]+6)%8]:
        isRotate[mgNum+1] = CW*(-1)
    rotate_right(mgNum+1, isRotate[mgNum+1])
    
def rotate_left(mgNum, CW):
    global magnet,mgPtr,isRotate    
    if mgNum == 0:
        return
    now = magnet[mgNum]
    next = magnet[mgNum-1]
    if next[(mgPtr[mgNum-1]+2)%8] != now[(mgPtr[mgNum]+6)%8]:
        isRotate[mgNum-1] = CW*(-1)
    rotate_left(mgNum-1, isRotate[mgNum-1])


for t in range(1, T+1):
    K = int(input())
    
    magnet = []
    mgPtr = [0, 0, 0, 0]
    for _ in range(4):
        magnet.append(list(map(int, input().split())))
    
    for _ in range(K):
        mgNum, CW = map(int, input().split())
        isRotate = [0, 0, 0, 0]
        isRotate[mgNum-1] = CW
        rotate_right(mgNum-1, CW)
        rotate_left(mgNum-1, CW)
        
        for i in range(4):
            mgPtr[i] = (mgPtr[i] - isRotate[i])%8
    ans = 0
    for i in range(4):
        if magnet[i][mgPtr[i]]:
            ans += 1<<i
            
    print(f"#{t} {ans}")