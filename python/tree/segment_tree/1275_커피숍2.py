### 커피숍2 (G1)
import sys
from math import log2, ceil
input = sys.stdin.readline

def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        init(arr, tree, node*2, start, (start+end)//2)
        init(arr, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

def query(tree, node, start, end, left, right):
    if end < left or start > right:
        return 0
    if left <= start and end <= right:
        return tree[node]
    else:
        lsum = query(tree, node*2, start, (start+end)//2, left, right)
        rsum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
        return lsum+rsum

def update(arr, tree, node, start, end, index, value):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = value
        arr[index] = value
        return
    else:
        update(arr, tree, node*2, start, (start+end)//2, index, value)
        update(arr, tree, node*2+1, (start+end)//2+1, end, index, value)
        tree[node] = tree[node*2] + tree[node*2+1]

N, M = map(int, input().split())
arr = list(map(int, input().split()))
height = ceil(log2(N))
tree_size = 1<<(height+1)
tree = [0]*tree_size
init(arr, tree, 1, 0, N-1)

for i in range(M):
    x, y, a, b = map(int, input().split())
    if y < x:
        x, y = y, x
    print(query(tree, 1, 0, N-1, x-1, y-1))
    update(arr, tree, 1, 0, N-1, a-1, b)