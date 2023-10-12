### 트라이 (trie)
### 14425) 문자열 집합 (S3)
import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, isEnd):
        self.isEnd = isEnd
        self.childNode = {}

class Trie(object):
    def __init__(self):
        self.parent = Node(None)

    def insert(self, string):
        now = self.parent
        tmp_len = 0
        for ch in string:
            if ch not in now.childNode:
                now.childNode[ch] = Node(ch)
            now = now.childNode[ch]
            tmp_len += 1
            if tmp_len == len(string):
                now.isEnd = True
    
    def search(self, string):
        now = self.parent
        tmp_len = 0
        for ch in string:
            if ch in now.childNode:
                now = now.childNode[ch]
                tmp_len += 1
                if tmp_len == len(string) and now.isEnd == True:
                    return True
            else:
                return False
        return False
    
N, M = map(int, input().split())
trie = Trie()
for _ in range(N):
    tmp = input().strip()
    trie.insert(tmp)
ans = 0
for _ in range(M):
    tmp = input().strip()
    if trie.search(tmp):
        ans += 1
        
print(ans)