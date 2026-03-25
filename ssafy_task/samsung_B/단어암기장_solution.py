from heapq import heappush, heappop
N = 0
M = 0
T = []
# {단어 아이디: (행, 열, 길이)}
words = {}
# row_words[행번호]: (시작열, 끝열)
row_words = []



def init(n:int, m:int) -> None:
    N = n
    M = m
    T = [M] * (N*4)
    # 1-based, 행번호는 1부터 시작
    row_words = [[] for _ in range(N+1)]
    
# 가장 위쪽에 위치한 행번호 찾는 메서드
def find(node, cs, ce, val):
    if cs == ce:
        return cs # 행번호 리턴
    
    mid = (cs + ce) // 2
    if T[node*2] >= val: 
        return find(node*2, cs, mid, val)

    if T[node*2+1] >= val:
        return find(node*2+1, mid+1, ce, val)
    
    # 현재 단어를 넣을 수 없으면
    return -1

# 최대 빈칸 길이에 변동이 생긴 경우 업데이트
def update(node, cs, ce, idx, val):
    # 수정할 필요가 없는 노드면 나감
    if idx < cs or idx > ce: return
    # 리프 도달
    if cs == ce:
        T[node] = val
        return
    
    mid = (cs + ce) // 2
    # 좌우 자식 업데이트하고
    update(node*2, cs, mid, idx, val)
    update(node*2+1, mid + 1, ce, idx, val)
    # 자식들의 맥스값을 자신의 값으로 변경
    T[node] = max(T[node*2], T[node*2+1])
    
    return

def writeWord(mId:int, mLen:int) -> int:
    row = find(1, 1, N, mLen)
    if row == -1: return -1
    
    
    
    
    
    # # row에 단어를 기록
    
    # # 해당 열에 아무 단어가 없는 경우 걍 맨앞에 쓰자
    # if len(row_words[row]) == 0:
    #     # one-based
    #     row_words[row].append((1, mLen))
    #     update(1, 1, N, row, N-mLen)
    
    # # 해당 열에 단어가 하나만 있는 경우
    # elif len(row_words[row]) == 1:
    #     single = row_words[row][0]
        
    #     # 이러면 현재 단어 앞에 기록 가능
    #     if single[0] > mLen:
    #         heappush(row_words[row], (1, mLen))
    #         # 빈 공간 체크 (삽입단어 ~ 원래있었던단어 공간, 오른쪽여백 비교)
    #         space = max((single[0] - mLen - 1), (M - single[1]))
    #         update(1, 1, N, row, space)
        
    #     # 현재 단어 뒤에 기록
    #     else:
    #         heappush(row_words[row], (single[1]+1, single[1]+mLen))
    #         # 시작~단어1, 단어2~끝 공간비교
    #         space = max((single[0] - 1), (M - (single[1]+mLen)))
    #         update(1, 1, N, row, space)
    
    # # 해당 열에 단어가 두 개 이상인 경우
    # else:
    #     fit = False
    #     # first: 다음 단어가 들어갈 공간, space_max: 세그트리에 반영할 공간
    #     space_first = row_words[row][0][0]-1
    #     fit_col = 0
    #     space_max = space_first
    #     max_col = 1
    #     if space_first <= mLen:
    #         fit = True
    #         fit_col = 1
    #     # 단어 사이를 순회해 first fit을 찾자
    #     for i in range(len(row_words[row]) - 1):
    #         one = row_words[row][i]
    #         two = row_words[row][i+1]
    #         tmp_space = two[0] - one[1] - 1

    #         if not fit and tmp_space >= mLen:
    #             fit = True
    #             space_first = tmp_space
    #             fit_col = one[1]+1
            
    #         if tmp_space > space_max:
    #             space_max = tmp_space
    #             max_col = one[1]+1
        
    #     # 맨 마지막 공간까지 체크
    #     tmp_space = M - row_words[row][-1][1]
    #     if not fit and tmp_space >= mLen:
    #         fit = True
    #         space_first = tmp_space
    #         fit_col = row_words[row][-1][1] + 1
    #     if tmp_space > space_max:
    #         space_max = tmp_space
    #         max_col = one[1]+1
            
    #     heappush(row_words[row], (fit_col, fit_col+mLen-1))
        
    #     # 가장 큰 공간에 단어를 넣었다면
    #     if fit_col == max_col:
            
        
        
    # # dict에 단어를 기록
    # words[mId] = (row, _, mLen)

    
    # # row를 리턴
    
    

def eraseWord(mId:int) -> int:
    return -1
