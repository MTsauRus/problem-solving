### 최대 힙
class Heap:
    def __init__(self): ## heap[0]에 None 삽입.
        self.heap = []
        self.heap.append(None) 

    def check_swap_up(self, idx): # 부모와의 스왑이 필요한지 체크
        # 부모 노드가 없을 경우
        if idx <= 1:
            return False
        
        parent_idx = idx // 2

        if self.heap[idx] > self.heap[parent_idx]:
            return True # 자식이 부모보다 크다면
        else:
            return False
        
    def insert(self, data):
        self.heap.append(data) # heap의 끝부분에 data 삽입.
        idx = len(self.heap) - 1 # idx의 맨 앞에 0을 삽입했으므로.

        # check_swap_up()이 true이면 부모와 스왑
        while self.check_swap_up(idx):
            parent_idx = idx // 2 # 부모의 idx

            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx

        return True
    ### 삭제 연산 ###
    # 루트 노드를 제거하고, 말단 노드를 루트로 올린 후, 자식과 대소 비교 진행.
    # 자식이 없는 경우, 둘 다 있는 경우, 한쪽만 있는 경우 모두를 고려
    def check_swap_down(self, idx):
        left_idx = idx * 2
        right_idx = idx * 2 + 1
        # 자식 노드가 없는 경우
        if left_idx >= len(self.heap):
            return False
        # 왼쪽 자식만 있는 경우
        elif right_idx >= len(self.heap):
            if self.heap[left_idx] > self.heap[idx]:
                self.flag = 1
                return True
            else:
                return False
        # 자식 노드가 모두 있는 경우
        else: 
            if self.heap[left_idx] > self.heap[right_idx]:
                if self.heap[left_idx] > self.heap[idx]:
                    # 왼쪽 자식이 가장 큰 경우
                    self.flag = 1
                    return True
                else: # 왼쪽 자식이 더 크지만 부모가 더 크면 스왑 x
                    return False
            else: 
                if self.heap[right_idx] > self.heap[idx]:
                    # 오른쪽 자식이 가장 큰 경우
                    self.flag = 2
                    return True
                else:
                    return False
    
    def pop(self):
        if len(self.heap) <= 1:
            return None
        
        max = self.heap[1] # 현재 최대 값: 루트 노드
        self.heap[1] = self.heap[-1] # 말단 노드를 루트에 저장
        del self.heap[-1] # 말단 노드 제거
        idx = 1 # 현재 idx는 루트임.

        # flag
        # 0 = False, 1 = left swap, 2 = right swap
        self.flag = 0

        while self.check_swap_down(idx):
            left_idx = idx * 2
            right_idx = idx * 2 + 1

            if self.flag == 1: # left swap
                self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
                idx = left_idx
            elif self.flag == 2: # right swap
                self.heap[idx], self.heap[right_idx] = self.heap[right_idx], self.heap[idx]
                idx = right_idx
        return max
                 
#############
#최소힙
##############
import sys
from collections import deque
input = sys.stdin.readline

class Heap:
    def __init__(self): ## heap[0]에 None 삽입.
        self.heap = []
        self.heap.append(None) 

    def isEmpty(self): # 힙이 비었는지 확인.
        if not self.heap:
            return True
        else:
            return False
        
    def check_swap_up(self, idx): # 부모와의 스왑이 필요한지 체크
        # 부모 노드가 없을 경우
        if idx <= 1:
            return False
        
        parent_idx = idx // 2

        if self.heap[idx] < self.heap[parent_idx]:
            return True # 부모가 자식보다 크다면
        else:
            return False
        
    def insert(self, data):
        self.heap.append(data) # heap의 끝부분에 data 삽입.
        idx = len(self.heap) - 1 # idx의 맨 앞에 0을 삽입했으므로.

        # check_swap_up()이 true이면 부모와 스왑
        while self.check_swap_up(idx):
            parent_idx = idx // 2 # 부모의 idx

            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx

        return True
    ### 삭제 연산 ###
    # 루트 노드를 제거하고, 말단 노드를 루트로 올린 후, 자식과 대소 비교 진행.
    # 자식이 없는 경우, 둘 다 있는 경우, 한쪽만 있는 경우 모두를 고려
    def check_swap_down(self, idx):
        left_idx = idx * 2
        right_idx = idx * 2 + 1
        # 자식 노드가 없는 경우
        if left_idx >= len(self.heap):
            return False
        # 왼쪽 자식만 있는 경우
        elif right_idx >= len(self.heap):
            if self.heap[left_idx] < self.heap[idx]: # 왼쪽 자식이 더 크다면
                self.flag = 1
                return True
            else:
                return False
        # 자식 노드가 모두 있는 경우
        else: 
            if self.heap[left_idx] < self.heap[right_idx]:
                if self.heap[left_idx] < self.heap[idx]:
                    # 왼쪽 자식이 가장 작은 경우
                    self.flag = 1
                    return True
                else: # 왼쪽 자식이 작지만 부모가 더 작으면 스왑 x
                    return False
            else: 
                if self.heap[right_idx] < self.heap[idx]:
                    # 오른쪽 자식이 가장 작은 경우
                    self.flag = 2
                    return True
                else:
                    return False
    
    def pop(self):
        if len(self.heap) <= 1:
            return 0
        
        max = self.heap[1] # 현재 최대 값: 루트 노드
        self.heap[1] = self.heap[-1] # 말단 노드를 루트에 저장
        del self.heap[-1] # 말단 노드 제거
        idx = 1 # 현재 idx는 루트임.

        # flag
        # 0 = False, 1 = left swap, 2 = right swap
        self.flag = 0

        while self.check_swap_down(idx):
            left_idx = idx * 2
            right_idx = idx * 2 + 1

            if self.flag == 1: # left swap
                self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
                idx = left_idx ## 이거때매 틀린듯?
            elif self.flag == 2: # right swap
                self.heap[idx], self.heap[right_idx] = self.heap[right_idx], self.heap[idx]
                idx = right_idx ## 제발
        return max
