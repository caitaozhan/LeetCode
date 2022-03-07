#
# @lc app=leetcode id=1359 lang=python3
#
# [1359] Count All Valid Pickup and Delivery Options
#

from math import comb

# @lc code=start
class Solution:
    def countOrders(self, n: int) -> int:
        # def comb(n, k):
        #     numerator = 1
        #     denomenator = 1
        #     for i in range(k):
        #         numerator *= (n - i)
        #         denomenator *= (i + 1)
        #     return numerator // denomenator

        mod = 10**9 + 7
        ans = 1
        for num in range(2 * n, 0, -2):
            ans = (ans * comb(num, 2)) % mod
        return ans

        
# @lc code=end

