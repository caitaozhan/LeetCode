#
# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#

from collections import defaultdict
from typing import List

# @lc code=start
class Solution:
    '''O(k n^2) solution, TLE
    '''
    def minimumLengthEncoding(self, words: List[str]) -> int:

        def suffix_substring(a, b):
            '''return true if a is suffix substring of b, 
               i.e., a = 'cat', b = 'bobcat'
            '''
            if len(a) >= len(b):
                return False
            i = len(a) - 1
            j = len(b) - 1
            while i >= 0:
                if a[i] != b[j]:
                    return False
                i -= 1
                j -= 1
            return True

        mydict = defaultdict(set)
        for word in words:
            mydict[word].add(word)
        
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] == words[j]:
                    continue
                if suffix_substring(words[j], words[i]):
                    if words[j] in mydict:
                        mydict.pop(words[j])
        
        ans = 0
        for key in mydict.keys():
            ans += len(key)
            ans += 1
        return ans

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ans = 0
    
    def insert(self, word: str):
        '''inserts a word into the trie
        '''
        new_node = False
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
                new_node = True
            cur = cur.children[ch]
            cur.isEndOfWord = False
        if new_node:
            cur.isEndOfWord = True
    
    def count(self):
        '''count the isEndOfWord and multiply the length accordingly
        '''
        def dfs(root, depth):
            if root:
                if root.isEndOfWord:
                    self.ans += (depth + 1)
                    return
                for child in root.children:
                    dfs(root.children[child], depth+1)
        
        dfs(self.root, 0)


class Solution:
    '''O(kn) solution using a Trie
    '''
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)  # remove duplicate words
        trie = Trie()
        for word in words:
            trie.insert(word[::-1])
        trie.count()
        return trie.ans

# @lc code=end

