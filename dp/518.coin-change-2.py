#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#
# https://leetcode.com/problems/coin-change-2/description/
#
# algorithms
# Medium (49.66%)
# Likes:    2006
# Dislikes: 62
# Total Accepted:    133.4K
# Total Submissions: 267.6K
# Testcase Example:  '5\n[1,2,5]'
#
# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that
# amount. You may assume that you have infinite number of each kind of
# coin.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# Example 2:
# 
# 
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# 
# 
# Example 3:
# 
# 
# Input: amount = 10, coins = [10] 
# Output: 1
# 
# 
# 
# 
# Note:
# 
# You can assume that
# 
# 
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    '''Remember the outer loop is iterating through the coins
       It's like the knapsack problem, iterating throught the coins in the outer loop,
       so that there is an 'order'. This order prevents the duplicatet solutions
    '''
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]


class SolutionWrong:
    '''This will lead to duplicate solutions
       but this is the correct solution to #377.combination-sum-iv
    '''
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] += dp[i-coin]
        return dp[amount]

# @lc code=end

