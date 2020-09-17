#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (49.74%)
# Likes:    1980
# Dislikes: 372
# Total Accepted:    257.1K
# Total Submissions: 487.6K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,3,2]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [0,1,0,1,0,1,99]
# Output: 99
# 
#

from typing import List

# @lc code=start
class Solution:
    ''' https://medium.com/@lenchen/leetcode-137-single-number-ii-31af98b0f462
    '''
    def singleNumber(self, nums: List[int]) -> int:
        h, l = 0, 0
        for i in nums:
            l = ~h & (l ^ i)
            h = ~l & (h ^ i)
        return l

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2
# @lc code=end

