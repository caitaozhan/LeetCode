#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if not stack:    # check if empty
                    return False
                if ch == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif ch == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                elif ch == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        if not stack:
            return True  # stack is empty
        else:
            return False

# @lc code=end

