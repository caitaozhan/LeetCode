#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (53.60%)
# Likes:    2143
# Dislikes: 184
# Total Accepted:    463.6K
# Total Submissions: 845.1K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#

from typing import List

# @lc code=start
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        dictint = defaultdict(int)
        for n in nums:
            dictint[n] += 1
        for key, val in dictint.items():
            if val > len(nums)/2:
                return key

class Solution:
    '''
    This is a o(n) time and O(1) space solution form http://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html
    The solution is inspired from the strong assumption that the majority indeed exists.
    After one pass, only the majority can "survive"
    '''
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        counter  = 0
        for n in nums:
            if counter == 0:
                majority = n
                counter = 1
            else:
                if n == majority:
                    counter += 1
                else:
                    counter -= 1
        return majority


class Solution:
    ''' A slightly different implementation of boyer moore
    '''
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == major:
                count += 1
            else:
                count -= 1
                if count == 0:
                    major = nums[i]
                    count = 1
        return major

# @lc code=end

