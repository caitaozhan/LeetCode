#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def __init__(self):
        self.dp = {0: 1, 1: 1}

    def numTrees(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]

        ans = 0
        for i in range(n):
            ans += self.numTrees(i) * self.numTrees(n-1-i)
        self.dp[n] = ans
        return ans


n = 8
s = Solution()
print(s.numTrees(n))

# @lc code=end

