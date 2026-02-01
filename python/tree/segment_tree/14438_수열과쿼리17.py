### 수열과 쿼리 17 (G1)
import sys
from math import log2, ceil
input = sys.stdin.readline
MAX = 10**9

def init(arr, tree, node, start, end):
    if start == end: # leaf node
        tree[node] = arr[start]
        return

    init(arr, tree, node*2, start, (start + end)//2) # left child
    init(arr, tree, node*2+1, (start + end)//2+1, end) # right child
    tree[node] = min(tree[node*2], tree[node*2+1]) # 구간에서의 min 값

def query(tree, node, start, end, left, right): # return min
    if left > end or right < start:
        return MAX
    if left <= start and end <= right: # 범위 안에 들어온 경우
        return tree[node] # [start, end]의 최솟값 리턴
    lmin = query(tree, node*2, start, (start+end)//2, left, right) # min of left child
    rmin = query(tree, node*2+1, (start+end)//2+1, end, left, right) # min of right child
    return min(lmin, rmin)

def update(arr, tree, node, start, end, index, value):
    if index < start or index > end: # 범위 벗어나는 것 먼저 판단!!! 아래 케이스와 순서 바뀔 시 오답
        return
    if start == end: # leaf node. 즉 tree[node] == arr[index] == value
        arr[index] = value
        tree[node] = value
        return
    update(arr, tree, node*2, start, (start+end)//2, index, value)
    update(arr, tree, node*2+1, (start+end)//2+1, end, index, value)
    tree[node] = min(tree[node*2], tree[node*2+1])
    
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
H = ceil(log2(N))
tree_size = 1<<(H+1)
tree = [0] * tree_size
init(arr, tree, 1, 0, N-1)
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1: # update
        update(arr, tree, 1, 0, N-1, b-1, c)
    else: # print min
        print(query(tree, 1, 0, N-1, b-1, c-1))
    