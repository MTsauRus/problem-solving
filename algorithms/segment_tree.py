import math
### 세그먼트 트리 ### 
# init
# node: start~end까지의 합
def init(arr, tree, node, start, end): 
    if start == end: # 리프 노드를 의미함.
        tree[node] = arr[start]
    else:
        # 예를 들어, node에 저장된 값이 0-3이라 한다면
        # 왼쪽 노드는 0-1, 오른쪽 노드는 2-3이 저장된다. 
        # 이를 일반화하였을 때 (start ~ (start+end)//2), ((start+end)//2+1 ~ end)이다. 
        init(arr, tree, node*2, start, (start+end)//2) # 왼쪽 자식
        init(arr, tree, node*2+1, (start+end)//2+1, end) # 오른쪽 자식
        tree[node] = tree[node*2] + tree[node*2+1]




















l = [1, 2, 3, 4, 5, 6, 7 ,8]
h = math.ceil(math.log2(len(l)))
tree_size = 1<<(h+1)
tree = [0]*tree_size
start=0
end=7
init(l,tree,1,start,end)
print(tree)
