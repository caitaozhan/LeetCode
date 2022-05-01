#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

from typing import List

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dfs(stack, path, left_count, n):
            if len(path) == 2*n:
                ans.append(path)
                return
            if not stack:
                path += '('
                left_count += 1
                dfs(stack + ['('], path, left_count, n)
            else:
                if left_count == n:   # '(' is full
                    path += ')'
                    dfs(stack[:-1], path, left_count, n)
                else:
                    # put '('
                    path += '('
                    left_count += 1
                    dfs(stack + ['('], path, left_count, n)
                    path = path[:-1]
                    left_count -= 1

                    # put ')'
                    path += ')'
                    dfs(stack[:-1], path, left_count, n)

        stack = []
        path = ''
        left_count = 0   # counter of the left parentheses
        ans = []
        dfs(stack, path, left_count, n)
        return ans

n = 3
s = Solution()
print(s.generateParenthesis(n))

        
# @lc code=end

