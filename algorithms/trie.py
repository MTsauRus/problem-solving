### 트라이 (trie)
### 14425) 문자열 집합 (S3)
import sys
input = sys.stdin.readline

class Node(object): # 노드 클래스 
    def __init__(self, isEnd): # Node 객체 생성 시 실행
        self.isEnd = isEnd  # insert에서 param으로 넘겨줌. string의 마지막 ch라면 True를, 아니라면 ch를 저장한다. 
        self.childNode = {} # 자식 노드를 dict 형식으로 관리

class Trie(object): # 트라이 클래스
    def __init__(self): # Trie 객체 생성 시 실행
        self.parent = Node(None) # parent 지역 변수. 루트 노드를 None으로 생성

    def insert(self, string): # 삽입 메소드 
        now = self.parent # 현재 노드를 의미. 
        tmp_len = 0 # 현재 길이를 의미
        for ch in string: # param으로 넘어온 str를 ch 단위로 쪼갬
            if ch not in now.childNode: # 만약 ch가 현재 자식 노드 dict에 존재하지 않다면
                now.childNode[ch] = Node(ch) # 현재 노드의 자식에 ch 노드를 만들자. 
            now = now.childNode[ch] # 그리고 자식 노드로 이동
            tmp_len += 1 # 문자열 길이를 1 증가시킨다. 
            if tmp_len == len(string): # 만약 insert iter 수가 문자열 길이와 같다면 ( == 문자열을 끝까지 저장했다면)
                now.isEnd = True # 현재 노드의 isEnd를 True라고 표기한다. 
    
    def search(self, string): # 트라이에서 문자열을 탐색하는 메소드 
        now = self.parent # 루트 노드에서부터 탐색을 시작한다. 
        tmp_len = 0 # 현재 문자열 길이
        for ch in string: # 문자열을 ch 단위로 쪼갬
            if ch in now.childNode: # 현재 ch가 자식 노드에 존재한다면
                now = now.childNode[ch] # 자식 노드로 이동하고
                tmp_len += 1 # 문자열 길이를 1 증가시킨다. 
                if tmp_len == len(string) and now.isEnd == True: # 만약 문자열 길이가 input 길이와 같고, 현재 ch가 string의 끝이라면.
                                                                 # ( 해당 문자열이 이미 트라이 내에 저장되어 있었다면)
                    return True # True를 반환한다. 
            else:
                return False # input: as, 트라이에 저장되어 있는 string: asd와 같은 경우. 
        return False # 입력된 string의 len이 0인 경우. (예외처리)
    
N, M = map(int, input().split()) # 문제 풀이 부분. 저장될 문자열 수 N, 검사할 문자열 수 M
trie = Trie() # 트라이 객체 생성
for _ in range(N):
    tmp = input().strip()
    trie.insert(tmp) 
ans = 0
for _ in range(M):
    tmp = input().strip()
    if trie.search(tmp):
        ans += 1
        
print(ans)