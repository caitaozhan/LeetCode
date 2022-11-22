#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

import math

class PerfectSquares:
    '''precomputation, O(n**1.5)
    '''
    def __init__(self):
        n = 10**4
        self.dp = [float('inf')] * (n + 1)
        self.dp[0] = 0
        ub = int(math.sqrt(n))
        coins = sorted([i ** 2 for i in range(1, ub + 1)], reverse=True)
        for coin in coins:
            for i in range(coin, n + 1):
                self.dp[i] = min(self.dp[i], self.dp[i - coin] + 1)


# @lc code=start
class Solution:
    perfect_squares = PerfectSquares()

    def numSquares(self, n: int) -> int:
        return Solution.perfect_squares.dp[n]


n = 17
s = Solution()
print(s.numSquares(n))

# @lc code=end

