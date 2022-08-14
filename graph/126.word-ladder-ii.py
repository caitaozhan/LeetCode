#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

from typing import List
from collections import defaultdict
from functools import lru_cache

# @lc code=start
class Solution:
    # using lru_cache consumes more memory, but faster
    @lru_cache(None)
    def template(self, word: str, i: int) -> str:
        return word[:i] + '*' + word[i+1:]

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # step 1: initialization
        wordList = list(set(wordList + [beginWord]))
        n = len(beginWord)
        dist = {}
        for word in wordList:
            dist[word] = float('inf')
        if endWord not in dist:
            return []
        graph = defaultdict(list)
        for word in wordList:
            for i in range(n):
                temp = self.template(word, i)
                graph[temp].append(word)
        
        # step 2: BFS
        prevnode = defaultdict(list)
        queue = [endWord]
        dist[endWord] = 0
        found = False
        while queue and not found:
            new_queue = []
            for cur in queue:
                for i in range(n):
                    temp = self.template(cur, i)
                    for nxt in graph[temp]:
                        if dist[nxt] == float('inf'):    # not visited
                            dist[nxt] = dist[cur] + 1
                            new_queue.append(nxt)
                            prevnode[nxt].append(cur)
                        elif dist[nxt] == dist[cur] + 1: # visited, two nodes at the same distance visited nxt
                            prevnode[nxt].append(cur)
                        else:
                            pass
                        if nxt == beginWord:
                            found = True
            queue = new_queue
        

        # step 3: recover the paths by DFS
        if not found:
            return []

        def dfs(node, stack):
            stack.append(node)
            if len(prevnode[node]) == 0:
                ans.append(stack.copy())
            for nxt in prevnode[node]:
                dfs(nxt, stack)
                stack.pop()
        ans = []
        dfs(beginWord, stack=[])
        return ans


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

beginWord = "a"
endWord = "c"
wordList = ["a", "b", "c"]

s = Solution()
print(s.findLadders(beginWord, endWord, wordList))


        
# @lc code=end

