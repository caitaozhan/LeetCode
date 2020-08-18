#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (50.13%)
# Likes:    5593
# Dislikes: 244
# Total Accepted:    923.6K
# Total Submissions: 1.8M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
# 
# Note that you cannot sell a stock before you buy one.
# 
# Example 1:
# 
# 
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# 
# 
# Example 2:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 
#

from typing import List

# @lc code=start
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minarr = [float('inf')]*len(prices)
        minarr[0] = prices[0]
        for i in range(len(prices)):
            minarr[i] = min(minarr[i-1], prices[i])
        maxp = float('-inf')
        ans = 0
        for i, p in reversed(list(enumerate(prices))):
            maxp = max(maxp, p)
            ans = max(ans, maxp-minarr[i])
        return ans


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minprice = float('inf')
        ans = 0
        for p in prices:
            minprice = min(minprice, p)
            ans = max(0, ans, p - minprice)
        return ans


# if __name__ == '__main__':
#     prices = [7,1,5,3,6,4]
#     s = Solution()
#     print(s.maxProfit(prices))
# @lc code=end

