#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#

class Solution:
    '''greedy, buy the cheapest ice creams first
    '''
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for c in costs:
            if c <= coins:
                ans += 1
                coins -= c
            else:
                break
        return ans

