### 최솟값 (G1)
import sys
input = sys.stdin.readline
from math import log2, ceil
MAX = 10**9

def init(arr, tree, node, start, end):
    if start == end: # leaf node
        tree[node] = arr[start]
    else:
        init(arr, tree, node*2, start, (start+end)//2) # left child
        init(arr, tree, node*2+1, (start+end)//2+1, end) # right child
        tree[node] = min(tree[node*2], tree[node*2+1])

def query(tree, node, start, end, left, right):
    if right < start or left > end:
        return MAX
    if left <= start and end <= right:
        return tree[node]
    lmin = query(tree, node*2, start, (start+end)//2, left, right)
    rmin = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return min(lmin, rmin)
    
        

N, M = map(int, input().split())
arr = list(int(input()) for _ in range(N))
height = ceil(log2(N))
tree_size = 1<<(height+1)
tree = [0] * tree_size
init(arr, tree, 1, 0, N-1)
for i in range(M):
    a, b = map(int, input().split())
    print(query(tree, 1, 0, N-1, a-1, b-1))
