#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (30.27%)
# Likes:    2638
# Dislikes: 140
# Total Accepted:    264.6K
# Total Submissions: 867.2K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# Example:
# 
# 
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# Note:
# 
# You can assume that you can always reach the last index.
# 
#

from typing import List

# @lc code=start
class Solution2:
    '''dp. note that the len(nums) can go up to 3*10^4, so O(n^2) will not work
       TLE
    '''
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n-1]

class Solution3:
    '''dp. this is actually also O(n^2) in the worst case
       TLE
    '''
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        for i, max_len in enumerate(nums):
            for j in range(i, i + max_len + 1):
                if j == n:
                    break
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[n-1]


class Solution4:
    '''this is an O(nlogn) solution by utilizing binary search
       accepted
    '''
    def bin_search(self, dp, i):
        low, high = 0, len(dp) - 1
        while low < high:
            mid = (low + high) // 2
            if dp[mid][0] >= i:
                high = mid
            else:
                low = mid + 1
        return dp[low][1]

    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        dp = [(0, 0)]  # (loc, min_num)
        for i, max_step in enumerate(nums):
            min_num = self.bin_search(dp, i)
            max_i = i + max_step
            if max_i >= len(nums) - 1:
                return min_num + 1
            if max_i > dp[-1][0]:
                dp.append((max_i, min_num + 1))


class Solution:
    '''dp. this is a smart dp.
    '''
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        dp = [0]
        max_i = 0
        for i, step in enumerate(nums):
            if i + step > max_i:
                dp.extend([dp[i]+1] * (i + step - max_i))
                max_i = i + step
                if len(dp) >= len(nums):
                    return dp[len(nums)-1]
                            
# @lc code=end
