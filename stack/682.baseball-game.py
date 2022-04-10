#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for x in ops:
            if x == 'C':
                stack.pop()
            elif x == 'D':
                stack.append(2*stack[-1])
            elif x == '+':
                stack.append(stack[-2] + stack[-1])
            else:
                stack.append(int(x))
        return sum(stack)
        
# @lc code=end

