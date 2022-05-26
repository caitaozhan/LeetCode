#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (27.74%)
# Likes:    1615
# Dislikes: 101
# Total Accepted:    134.6K
# Total Submissions: 480.4K
# Testcase Example:  '2\n[2,4,1]'
#
# Say you have an array for which the i-th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most k
# transactions.
# 
# Note:
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit =
# 4-2 = 2.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit =
# 6-2 = 4.
# Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 =
# 3.
# 
# 
#

from typing import List

class SolutionMLE:
    def print(self, dp):
        for row in dp:
            print(row)
        print()

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        dp = [[0]*len(prices) for _ in range(k+1)]
        for i in range(1, k+1):                              # transaction i
            minn = float('inf')
            for j in range(1, len(prices)):                  # up to day j
                tmp = dp[i-1][j-2] if j >= 2 else 0          # previous subproblem
                minn = min(minn, prices[j-1] - tmp)          # buy at day j-1
                dp[i][j] = max(dp[i][j-1], prices[j] - minn) # the equation
            self.print(dp)
        return dp[k][len(prices)-1]

# @lc code=start
class SolutionTLE:
    def print(self, dp):
        for row in dp:
            print(row)
        print()

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1 or k == 0:
            return 0
        dp = [[0]*len(prices) for _ in range(2)]             # if range(k+1), then memory limit exceed
        upper = min(k, int(len(prices)/2))
        for i in range(1, upper+1):                          # transaction i
            minn = float('inf')
            for j in range(1, len(prices)):                  # up to day j
                tmp = dp[0][j-2] if j >= 2 else 0            # previous subproblem
                minn = min(minn, prices[j-1] - tmp)          # buy at day j-1
                dp[1][j] = max(dp[1][j-1], prices[j] - minn) # the equation
            # if i%100 == 0:
            #     self.print(dp)
            #     print(i)
            dp[0] = dp[1]
            if i == upper:
                return dp[1][len(prices)-1]
            dp[1] = [0]*len(prices)  # important


class Solution:
    '''O(kn) time and O(n) space
    '''
    def print(self, dp):
        for row in dp:
            print(row)
        print()

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1 or k == 0:
            return 0
        if k > len(prices)/2:                                # the trick
            ans = 0
            for i in range(1, len(prices)):
                ans += max(prices[i] - prices[i-1], 0)
            return ans    

        dp = [[0]*len(prices) for _ in range(2)]             # if range(k+1), then memory limit exceed
        for i in range(1, k+1):                              # transaction i
            minn = float('inf')
            for j in range(1, len(prices)):                  # up to day j
                tmp = dp[0][j-2] if j >= 2 else 0            # previous subproblem
                minn = min(minn, prices[j-1] - tmp)          # buy at day j-1
                dp[1][j] = max(dp[1][j-1], prices[j] - minn) # the equation
            dp[0] = dp[1]
            if i == k:
                return dp[1][len(prices)-1]
            dp[1] = [0]*len(prices)                          # important


class SolutionTLE2:
    ''' O(kn^2)
    '''
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        if k >= n//2:
            profit = 0
            for i in range(1, n):
                profit += max(0, prices[i] - prices[i-1])
            return profit

        dp = [[0 for _ in range(n)] for _ in range(k+1)]
        for i in range(1, k+1):
            for j in range(1, n):
                maxx = dp[i][j-1]
                for d in range(-1, j):
                    subproblem = dp[i-1][d] if d >= 0 else 0
                    profit = subproblem + prices[j] - prices[d+1]
                    if profit > maxx:
                        maxx = profit
                dp[i][j] = maxx
        return dp[k][n-1]


class Solution2:
    '''O(kn) time and O(kn) space
       need to optimize the more straight forward O(kn^2). 
       The observation is to rewrite the equation and find that there are redundancy in computation
       the equation: dp[i][j] = dp[i-1][k] + prices[j] - prices[k+1]   for -1 < k < j
       rewrite-1:    dp[i][j] = prices[j] + (dp[i-1][k] - prices[k+1]) for -1 < k < j  --> max of the ( ... )
       rewrite-2:    dp[i][j] = prices[j] + (prices[k+1] - dp[i-1][k]) for -1 < k < j  --> min of the ( ... )
       observe the above 2 rewrite, we see that 
       1. ( ... ) is independent of variable j. also i is fixed
       2. ( ... ) is bounded by j
       So, for every new j = j + 1, just keep doing max or min of the current ( ... ) and the previous max or min
    '''
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        if k >= n//2:
            profit = 0
            for i in range(1, n):
                profit += max(0, prices[i] - prices[i-1])
            return profit

        dp = [[0 for _ in range(n)] for _ in range(k+1)]
        for i in range(1, k+1):                                # ith transaction
            minn = float('inf')
            for j in range(1, n):
                subproblem = dp[i-1][j-2] if j >=2 else 0      # subproblem of the (i-1)th transaction by the (j-2)th day
                minn = min(minn, prices[j-1] - subproblem)     # buy at day j-1
                dp[i][j] = max(dp[i][j-1], prices[j] - minn)   # sell at day j, the equation
        return dp[k][n-1]


def test():
    k = 4
    prices = [1,2,5,9,4,1,7,4,1,5,3,7,9,6,4,7,1,6]

    s = SolutionTLE()
    print(s.maxProfit(k, prices))

    # s = SolutionMLE()
    # print(s.maxProfit(k, prices))

# test()

