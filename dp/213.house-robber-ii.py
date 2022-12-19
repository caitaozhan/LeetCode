#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

from typing import List

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp1 = [0] * n  # max money till i-th including [0]
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])

        dp2 = [0] * n  # max money till i-th excluding [0]
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])
        for i in range(3, n):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])

        return max(dp1[-2], dp2[-1])

        
        
# @lc code=end

