#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (45.12%)
# Likes:    5703
# Dislikes: 239
# Total Accepted:    709K
# Total Submissions: 1.6M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#

from typing import List

# @lc code=start
class Solution2:
    '''dynamic programming
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        nums.insert(0, 0)
        dp = [0 for _ in range(len(nums))]
        maxx = -2**64
        for i in range(1, len(nums)):
            if dp[i-1] >= 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
            maxx = max(dp[i], maxx)
        return maxx

class Solution:
    '''optimize time complexity to O(1)
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = float('-inf')
        ans = float('-inf')
        for n in nums:
            cur_max = max(cur_max + n, n)
            ans = max(ans, cur_max)
        return ans

# @lc code=end

