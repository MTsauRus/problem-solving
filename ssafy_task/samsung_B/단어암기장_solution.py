N = 0
M = 0
T = []
# {단어 아이디: (행, 열, 길이)}
words = {}
# row_words[행번호]: (시작열, 끝열)
row_words = []

def init(n:int, m:int) -> None:
    global N, M, T, row_words, words
    words.clear()
    N = n
    M = m
    T = [M] * (N*4)
    # 1-based, 행번호는 1부터 시작
    # 시작 노드, 끝노드 미리 저장해놈
    row_words = [[(-1, -1), (M, M)] for _ in range(N+1)]
    
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

    for i in range(len(row_words[row]) - 1):
        one = row_words[row][i]
        two = row_words[row][i+1]
        tmp_space = two[0] - one[1] - 1
        
        # first fit 찾기
        if mLen <= tmp_space:
            row_words[row].append((one[1]+1, one[1]+mLen))
            input_idx = one[1]+1
            break
    
    # 삽입 후 재정렬
    row_words[row].sort()
    
    # 최대 공간 찾기        
    large_space = 0
    for i in range(len(row_words[row]) - 1):
        one = row_words[row][i]
        two = row_words[row][i+1]
        tmp_space = two[0] - one[1] - 1
        
        if large_space < tmp_space:
            large_space = tmp_space
    
    # 세그트리 허용공간 업데이트
    update(1, 1, N, row, large_space)
    
    # dict에 노드 정보 넣기
    # (행번호, 열번호, 길이)
    words[mId] = (row, input_idx, mLen)
    
    # zero-base로 리턴
    return row-1

def eraseWord(mId:int) -> int:
    if mId > 50001: return -1
    if mId not in words.keys():
        return -1
    
    now_word = words[mId]
    # nr은 1-base, nc는 0-base, nl은 길이
    nr, nc, nl = now_word
    
    del words[mId]
    row_words[nr].remove((nc, nc + nl - 1))
    
    large_space = 0
    
    for i in range(len(row_words[nr]) - 1):
        one = row_words[nr][i]
        two = row_words[nr][i+1]
        tmp_space = two[0] - one[1] - 1
        
        if large_space < tmp_space:
            large_space = tmp_space
                   
    update(1, 1, N, nr, large_space)
    return nr - 1