#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # step 1: build gragh
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        # step 2: do a dfs
        self.find = False
        visited = [False] * n

        def dfs(cur):
            if self.find:
                return
            if cur == destination:
                self.find = True
                return
            for nxt in g[cur]:
                if visited[nxt] is False:
                    visited[nxt] = True
                    dfs(nxt)
        
        dfs(source)
        return self.find
        

        
# @lc code=end

