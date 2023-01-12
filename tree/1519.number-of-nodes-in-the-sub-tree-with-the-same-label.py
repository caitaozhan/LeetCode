#
# @lc app=leetcode id=1519 lang=python3
#
# [1519] Number of Nodes in the Sub-Tree With the Same Label
#

from typing import List
from collections import defaultdict, Counter

# @lc code=start
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        def dfs(root: int, parent: int) -> Counter:
            root_counter = Counter()
            root_counter[labels[root]] += 1
            for child in g[root]:
                if child == parent:
                    continue
                child_counter = dfs(child, root)
                root_counter += child_counter
            ans[root] = root_counter[labels[root]]
            return root_counter

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        ans = [0] * n
        _ = dfs(0, None)
        return ans

# @lc code=end
