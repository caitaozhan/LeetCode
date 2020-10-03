#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (41.71%)
# Likes:    3300
# Dislikes: 74
# Total Accepted:    287K
# Total Submissions: 687.9K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#

from typing import List
from bisect import bisect_left

# @lc code=start
class Solution2:
    '''
    input:      x[1, 2, ..., n]
    subproblem: dp[i] is the LIS of x[1, 2, ..., i]
    equation:   dp[i] = max_{1<=j<i} (dp[j] + 1), for x[i] > x[j]
    answer:     max_{1<=i<=n} dp[i]
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0: 
            return 0

        dp = [1 for _ in range(size)]
        for i in range(size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for n in nums:
            i = bisect_left(dp, n)
            if i == len(dp):
                dp.append(n)
            else:
                dp[i] = n
        return len(dp)


nums = [10,9,2,5,3,7,101,18]
s = Solution()
print(s.lengthOfLIS(nums))

# @lc code=end

