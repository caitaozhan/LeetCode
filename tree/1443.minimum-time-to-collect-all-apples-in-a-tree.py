#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        def dfs(root: int, stack: list, visited: set):
            for nxt in g[root]:
                if nxt in visited:
                    continue
                visited.add(nxt)
                if hasApple[nxt]:
                    for i in range(len(stack)-1):
                        myset.add((stack[i], stack[i+1]))
                    myset.add((stack[-1], nxt))
                dfs(nxt, stack + [nxt], visited)

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        myset = set()  # distict edges
        dfs(0, [0], set([0]))
        return len(myset) * 2


class Solution:
    '''no need for visited set, just need to avoid the parent
       a smarter way to compute the anser: compute the time for each child, use child time to compute parent time
    '''
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        def dfs(root: int, parent: int) -> int:
            root_time = 0
            for child in g[root]:
                if child == parent:
                    continue
                child_time = dfs(child, root)
                if hasApple[child] or child_time > 0:
                    root_time += (child_time + 2)
            return root_time

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        return dfs(0, None)

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]
s = Solution()
print(s.minTime(n, edges, hasApple))


# @lc code=end

