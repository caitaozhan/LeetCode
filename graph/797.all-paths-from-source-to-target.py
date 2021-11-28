#
# @lc app=leetcode id=797 lang=python3
# [797] All Paths From Source to Target
# @lc code=start

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(target, sol, stack):
            cur = stack[-1]
            for nxt in graph[cur]:
                stack.append(nxt)
                if nxt == target:
                    sol.append(stack.copy())
                dfs(target, sol, stack)
                stack.pop()

        target = len(graph) - 1
        sol = []
        stack = [0]
        dfs(target, sol, stack)
        return sol

        
# @lc code=end

