#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
class Solution:
    '''DP, O(n)
    subproblem: dp[i] is the number of ways to tile upto to 2xi
    equation:   dp[i] = dp[i-1] + dp[i-2] + 2*(dp[0] + ... + dp[i-3])
    '''
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        prefixsum = [0] * (n + 1)
        prefixsum[0] = 1
        prefixsum[1] = 2
        prefixsum[2] = 4
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + prefixsum[i-3] * 2
            prefixsum[i] = prefixsum[i-1] + dp[i]
        return dp[n] % (10**9 + 7)
        
# @lc code=end

