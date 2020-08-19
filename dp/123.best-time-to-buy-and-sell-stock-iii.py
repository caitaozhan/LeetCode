#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (36.88%)
# Likes:    2495
# Dislikes: 78
# Total Accepted:    238.1K
# Total Submissions: 620.3K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
# 
# 
# Example 3:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
#

from typing import List

# @lc code=start
class SolutionTLE:
    ''' O(kn^2) solution, k=2, TLE
    '''
    def print(self, dp):
        for row in dp:
            print(row)
        print()

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        dp = [[0]*len(prices) for _ in range(3)]
        for i in range(1, len(dp)):           # transaction i
            for j in range(1, len(dp[0])):    # up to day j
                for k in range(0, j):         # buy at day k, sell at day j
                    tmp = dp[i-1][k-1] if k > 0 else 0
                    dp[i][j] = max(dp[i][j], dp[i][j-1], tmp + prices[j] - prices[k]) # don't sell at day k or sell at day k
        return dp[2][len(prices)-1]


class Solution:
    ''' O(kn) solution, k=2
    '''
    def print(self, dp):
        for row in dp:
            print(row)
        print()

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        dp = [[0]*len(prices) for _ in range(3)]
        for i in range(1, len(dp)):                    # transaction i
            minn = float('inf')
            for j in range(1, len(dp[0])):             # sell at day j
                tmp = dp[i-1][j-2] if j >= 2 else 0    # previous subproblem
                minn = min(minn, prices[j-1] - tmp)    # buy at day j-1
                dp[i][j] = max(dp[i][j-1], prices[j] - minn)    # don't sell at day j or sell at day j
        return dp[2][len(prices)-1]

# prices = [1, 2, 3, 4, 5]
# s = Solution()
# print(s.maxProfit(prices))


# @lc code=end

