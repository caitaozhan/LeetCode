#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)  # i, j
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if word1[0] == word2[0] else 0
        for i in range(1, m):  # j fixed to 0
            if word1[i] == word2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n):  # i fixed to 0
            if word1[0] == word2[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j-1]
                
        for i in range(1, m):
            for j in range(1, n):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return m + n - 2*dp[m-1][n-1]


        
# @lc code=end

