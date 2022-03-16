#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # step 1: build the stack for removal
        stack = []  # put index in the stack
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack and s[stack[-1]] == '(':  # when ( matches )
                    stack.pop()
                else:
                    stack.append(i)
        
        # step 2: remove
        new_s = []
        j = 0
        for i, ch in enumerate(s):
            if j < len(stack) and i == stack[j]:  # elements in stack is increasing
                j += 1
            else:
                new_s.append(ch)
        
        return ''.join(new_s)

# @lc code=end

