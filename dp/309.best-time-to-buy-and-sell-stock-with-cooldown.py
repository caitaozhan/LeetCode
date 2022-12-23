#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

from typing import List

# @lc code=start
class Solution:
    '''O(n^2), DP
       subproblem: dp[i] is the max profit by the i th day.
    '''
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        for i in range(1, n):      # the i th day
            dp[i] = dp[i-1]        # no sell at i th day
            for j in range(i):     # buy at j-th day, sell at i th day
                subprob = dp[j-2] if j >= 2 else 0
                dp[i] = max(dp[i], subprob + prices[i] - prices[j])
        return dp[-1]


class Solution:
    '''optimizing the time complexity to O(n)
           max(subprob + prices[i] - prices[j]), 0 <= j < i 
       ==> prices[i] + max(subprob - prices[j]), 0 <= j < i
    '''
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        maxx = float('-inf')
        for i in range(1, n):                       # the i th day
            subprob = dp[i-3] if i >= 3 else 0
            maxx = max(maxx, subprob - prices[i-1]) # buy at i-1 th day
            dp[i] = max(dp[i-1], prices[i] + maxx)  # no sell at i th day, sell at i th day
        return dp[-1]



prices = [1,2,3,0,2]
s = Solution()
print(s.maxProfit(prices))


# @lc code=end

