#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (60.64%)
# Likes:    1832
# Dislikes: 117
# Total Accepted:    172K
# Total Submissions: 266.2K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an integer array nums, in which exactly two elements appear only once
# and all the other elements appear exactly twice. Find the two elements that
# appear only once. You can return the answer in any order.
# 
# Follow up: Your algorithm should run in linear runtime complexity. Could you
# implement it using only constant space complexity?
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,0]
# Output: [-1,0]
# 
# 
# Example 3:
# 
# 
# Input: nums = [0,1]
# Output: [1,0]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 30000
# Each integer in nums will appear twice, only two integers will appear once.
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for n in nums:
            bitmask ^= n

        count = 0
        bitmask_copy = bitmask     # bitmask = x^y
        while bitmask & 1 == 0:
            count += 1
            bitmask >>= 1
        diff = 1 << count          # the rightmost 1-bit, at this bit, x and y are different

        x = 0
        for n in nums:
            if n & diff:           # use diff to filter out one of x and y
                x ^= n
        return [x, bitmask_copy^x]



# @lc code=end

