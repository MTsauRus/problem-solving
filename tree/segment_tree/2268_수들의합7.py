import sys
input = sys.stdin.readline
from math import log2, ceil

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
    lsum = query(tree, node*2, start, (start+end)//2, left, right)
    rsum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return lsum + rsum

def update(arr, tree, node, start, end, index, val):
    if index < start or index > end:
        return 
    if start == end:
        arr[index] = val
        tree[node] = val
        return
    else:
        update(arr, tree, node*2, start, (start+end)//2, index, val)
        update(arr, tree, node*2+1, (start+end)//2+1, end, index, val)
        tree[node] = tree[node*2] + tree[node*2+1]
        return
    
N, M = map(int, input().split())
arr = [0]*N
height = ceil(log2(N))
tree_size = 1<<(height+1)
tree = [0]*tree_size
init(arr, tree, 1, 0, N-1)
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        if b > c:
            b, c = c, b
        print(query(tree, 1, 0, N-1, b-1, c-1))
    else:
        update(arr, tree, 1, 0, N-1, b-1, c)