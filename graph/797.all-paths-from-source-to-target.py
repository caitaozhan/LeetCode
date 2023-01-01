#
# @lc app=leetcode id=797 lang=python3
# [797] All Paths From Source to Target
# @lc code=start

from typing import List

class Solution:
    '''11/28/2021
    '''
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


class Solution:
    '''redo on 12/30/2022
       note that for a DAG, there is no need for visited[] array
    '''
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(cur: int, stack: list):
            if cur == self.target:
                sol.append(stack.copy())
                return
            for nxt in graph[cur]:
                dfs(nxt, stack + [nxt])
        
        sol = []
        n = len(graph)
        self.target = n-1
        visited = [0] * n
        dfs(0, [0])
        return sol


# @lc code=end

