### 평행사변형 (S4)
import sys
input = sys.stdin.readline

def length(xa, ya, xb, yb):
    return (((xa-xb)**2)+((ya-yb)**2))**0.5
    
xa, ya, xb, yb, xc, yc = map(int, input().split())

if (ya-yb)*(xb-xc)==(yb-yc)*(xa-xb):
    print(-1.0)
else:
    ab = length(xa,ya,xb,yb)
    bc = length(xb,yb,xc,yc)
    ac = length(xa,ya,xc,yc)
    abc=2*ab+2*bc
    bca=2*bc+2*ac
    cab=2*ac+2*ab
    ans=max([abc,bca,cab])-min([abc,bca,cab])
    print(ans)
    