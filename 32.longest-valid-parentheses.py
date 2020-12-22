#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (27.98%)
# Likes:    4262
# Dislikes: 157
# Total Accepted:    324.6K
# Total Submissions: 1.1M
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# 
# Example 1:
# 
# 
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# 
# 
# Example 2:
# 
# 
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# 
# 
# Example 3:
# 
# 
# Input: s = ""
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.
# 
# 
#

# @lc code=start
class Solution:
    '''using a stack and array. two pass.
    '''
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        array = [0] * len(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else: # s[i] == ')'
                if stack:  # there is some '(' in the stack
                    array[i] = 1
                    array[stack[-1]] = 1
                    stack.pop()
        # now the task is to count consequtive 1
        maxx = 0
        counter = 0 
        for i in range(len(s)):
            if array[i] == 1:
                counter += 1
                maxx = max(maxx, counter)
            else:
                counter = 0
        return maxx



class Solution2:
    '''dp solution. 
    intput:      s[1 ... n]
    subproblem:  dp[i] is the longest valid parentheses of s[1 ... i] that ends at i
    '''
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                if s[i - 1] == ')':
                    if (i - dp[i - 1] - 1) >= 0 and s[i - dp[i - 1] - 1] == '(':
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 1 - 1]
        return max(dp)

# @lc code=end

