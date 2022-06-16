#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand_center(i, j):
            left, right = 0, 0
            while i >=0 and j < len(s):
                if s[i] == s[j]:
                    left = i
                    right = j
                    i -= 1
                    j += 1
                else:
                    break
            return left, right
        
        ans_left, ans_right = 0, 0
        for i in range(len(s)):
            left, right = expand_center(i, i)
            if right - left > ans_right - ans_left:
                ans_right = right
                ans_left = left
            left, right = expand_center(i, i+1)
            if right - left > ans_right - ans_left:
                ans_right = right
                ans_left = left
                
        return s[ans_left:ans_right+1]

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = (0, 0)

        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1):
            dp[i][i+1] = 1 if s[i] == s[i+1] else 0
            if dp[i][i+1] == 1:
                if answer[1]-answer[0] < 1:
                    answer = (i, i+1)
        
        for length in range(2, n):
            for i in range(0, n-length):
                j = i + length
                
                if dp[i+1][j-1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    if answer[1]-answer[0] < length:
                        answer = (i, j)
                else:
                    dp[i][j] = 0
                    
        return s[answer[0]:answer[1]+1]


# @lc code=end

