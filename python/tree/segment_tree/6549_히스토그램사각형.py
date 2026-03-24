### 6549. 히스토그램에서 가장 큰 직사각형
### 세그 풀이
import sys
input = sys.stdin.readline

while True:
    arr = [0] + list(map(int, input().split()))
    if len(arr) == 1 and arr[0] == 0: break
    
    T = [0] * (len(arr)*4)
    
    def init(idx, cs, ce):
        if cs == ce:
            # (구간최소높이, 구간최대넓이)
            T[idx] = (arr[cs], arr[cs])
        else:
            mid = (cs + ce) // 2
            init(idx*2, cs, mid)
            init(idx*2+1, mid+1, ce)
            
            min_height = min(T[idx*2][0], T[idx*2+1][0])
            max_area = max(T[idx*2][1], T[idx*2+1][1])
            now_width = ce - cs + 1
            
            print(idx)
            T[idx] = (min_height, max(min_height*now_width, max_area))
    
    print(init(1, 1, len(arr)))
    
    # def query(idx, cs, ce, gs, ge):
    #     if ce < gs or cs > ge:
    #         return (float('inf'), -float('inf'))
    #     if gs <= cs and ce <= ge:
    #         return T[idx]
        
    #     mid = (cs + ce) // 2
    #     lres = query(idx*2, cs, mid, gs, ge)
    #     rres = query(idx*2+1, mid+1, ce, gs, ge)
        
    #     min_height = min(lres[0], rres[0])
    #     max_area = 
    