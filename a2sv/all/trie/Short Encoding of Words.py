class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for idx in range(len(word)-1, -1, -1):
            if word[idx] not in cur.children:
                cur.children[word[idx]] = TrieNode()
            cur = cur.children[word[idx]]
        cur.endOfWord = True
    
    def isPrefix(self, word):
        cur = self.root
        for idx in range(len(word)-1, -1, -1):
            if word[idx] not in cur.children:
                return False
            cur = cur.children[word[idx]]
        return True
    
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        count = 0
        words.sort(key=lambda x: -(len(x)))
        for word in words:
            if trie.isPrefix(word) == False:
                trie.insert(word)
                count += len(word) + 1
        return count