#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (35.11%)
# Likes:    1965
# Dislikes: 183
# Total Accepted:    163.5K
# Total Submissions: 443.2K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# 
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
#

from typing import List
# @lc code=start
class Solution:
    '''refer to problem 169 majority element.
       first I came up with a method that add 2 minus 1, but it couldn't work out on test case [1,2,2]
       the correct way of doing it is to keep track of the larest two majority at the same time,
       then check them on a second pass 
    '''
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        count1, count2 = 0, 0
        major1, major2 = None, None
        for n in nums:
            if n == major1:
                count1 += 1
            elif n == major2:
                count2 += 1
            elif count1 == 0:
                major1 = n
                count1 = 1
            elif count2 == 0:
                major2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        ans = []
        for maj in [major1, major2]:
            if nums.count(maj) > len(nums)/3:
                ans.append(maj)
        return ans
# @lc code=end

