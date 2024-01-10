### 구간 합 구하기 (G1)
import sys
from math import ceil, log2
input = sys.stdin.readline

# init segment tree
def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        init(arr, tree, node*2, start, (start+end)//2)
        init(arr, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

# return sum[left, right]
def query(tree, node, start, end, left, right):
    if right < start or left > end:
        return 0    
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, node*2, start, (start+end)//2, left, right)
    rsum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return lsum + rsum

# update arr[index] = val
def update(arr, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end: # leaf node
        tree[node] = val
        arr[index] = val # update arr, tree
        return
    update(arr, tree, node*2, start, (start+end)//2, index, val) # left child
    update(arr, tree, node*2+1, (start+end)//2+1, end, index, val) # right child
    tree[node] = tree[node*2] + tree[node*2+1]
    
N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
height = ceil(log2(N)) # tree height
tree_size = 1 << (height+1) # tree size = 2^(H+1)
tree = [0] * tree_size
init(arr, tree, 1, 0, N-1) # init node(root) = 1, [start, end] = [0, N-1]
for _ in range(M+K):
    a, b, c = map(int, input().split()) # a==1: arr[b] = c; a==2: sum[b,c]
    if a == 1: # update
        update(arr, tree, 1, 0, N-1, b-1, c)
    else: # sum
        print(query(tree, 1, 0, N-1, b-1, c-1))
        
        

    