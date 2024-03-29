#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#


from typing import List

# @lc code=start
class SolutionOPT:
    '''optimizing the space
    '''
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prepre_max = nums[0]
        pre_max = max(nums[:2])
        for i in nums[2:]:
            cur_max = max(prepre_max + i, pre_max)
            prepre_max, pre_max = pre_max, cur_max
        return pre_max

class Solution:
    '''dp, O(n)
    '''
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # print(dp)
        return dp[-1]


class Solution:
    '''redo on 12/16/2022
       dp[i] is the maximum money till robbing the ith house, O(n^2)
    '''
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            dp[i] = nums[i]
            for j in range(i - 1):
                dp[i] = max(dp[i], dp[j] + nums[i])
        return max(dp)


# @lc code=end

