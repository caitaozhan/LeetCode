#
# @lc app=leetcode id=2246 lang=python3
#
# [2246] Longest Path With Different Adjacent Characters
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    '''dfs, the complexity is O(nlogn) due to using a sorting, which can be avoided...
    '''
    def longestPath(self, parents: List[int], s: str) -> int:
        def dfs(root: int, parent: int) -> int:
            root_length = 1
            child_info = []     # (child path length, child char)
            for child in g[root]:
                if child == parent:
                    continue
                child_info.append((dfs(child, root), s[child]))
            
            valid_childs = []
            for child in child_info:
                if s[root] != child[1]:
                    valid_childs.append(child)
            # need the "top 2" childs
            valid_childs.sort(reverse=True)
            if len(valid_childs) >= 2:
                path_length = 1 + valid_childs[0][0] + valid_childs[1][0]  # ^ shape path
                root_length = 1 + valid_childs[0][0]
                self.ans = max(self.ans, path_length)  # path length must >= root length
            elif len(valid_childs) == 1:
                root_length = 1 + valid_childs[0][0]
                self.ans = max(self.ans, root_length)
            else: # len(valid_childs) == 0
                pass
            return root_length

        # build graph
        g = defaultdict(list)
        for i in range(1, len(parents)):
            g[i].append(parents[i])
            g[parents[i]].append(i)

        # do dfs
        self.ans = 1
        _ = dfs(0, None)
        return self.ans


class Solution:
    '''dfs, the complexity is O(nlogn) due to using a sorting, which can be avoided...
    '''
    def longestPath(self, parents: List[int], s: str) -> int:
        def dfs(root: int, parent: int) -> int:
            top_child_length, second_child_length = 0, 0
            for child in g[root]:
                if child == parent:
                    continue
                child_length = dfs(child, root)
                if s[root] == s[child]:
                    continue
                if child_length > top_child_length:
                    second_child_length = top_child_length
                    top_child_length = child_length
                elif child_length > second_child_length:
                    second_child_length = child_length

            path_length = 1 + top_child_length + second_child_length
            self.ans = max(self.ans, path_length)
            return 1 + top_child_length

        # build graph
        g = defaultdict(list)
        for i in range(1, len(parents)):
            g[i].append(parents[i])
            g[parents[i]].append(i)

        # do dfs
        self.ans = 1
        _ = dfs(0, None)
        return self.ans


parents = [-1,0,0,1,1,2]
s = "abacbe"

parents = [-1, 0, 0, 0]
s = "aabc"

so = Solution()
print(so.longestPath(parents, s))

# @lc code=end

