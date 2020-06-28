#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (44.22%)
# Likes:    1720
# Dislikes: 80
# Total Accepted:    88.8K
# Total Submissions: 200.6K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an array which consists of non-negative integers and an integer m, you
# can split the array into m non-empty continuous subarrays. Write an algorithm
# to minimize the largest sum among these m subarrays.
# 
# 
# Note:
# If n is the length of array, assume the following constraints are satisfied:
# 
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# 
# 
# 
# Examples: 
# 
# Input:
# nums = [7,2,5,10,8]
# m = 2
# 
# Output:
# 18
# 
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    ''' Binary search, the range is the range of the answer, i.e. [1, summation]
    '''
    def can_split(self, nums_sum, m, x):
        '''return True if is able to split the array nums (passing in the nums_sum, not the original nums) in to m subarrays with max sum being x
           return False otherwise
           split using greedy
        '''
        if m == 1:
            if nums_sum[-1] <= x:
                return True
            else:
                return False
        i = 0
        pre_sum = 0
        cur_sum = 0
        while i < len(nums_sum):
            cur_sum = nums_sum[i] - pre_sum
            if cur_sum > x:                    # keep adding elements until over x
                if i == 0 or (i!= 0 and pre_sum == nums_sum[i-1]):  # the current single element is larger than x
                    return False
                else:                          # do a split
                    pre_sum = nums_sum[i-1]
                    m -= 1
                    if m == 1:
                        if nums_sum[-1] - pre_sum <= x:             # check the last subarray
                            return True
                        else:
                            return False
            else:
                i += 1
        return True

    def splitArray(self, nums: List[int], m: int) -> int:
        low = 1
        high = sum(nums)
        nums_sum = [0]*len(nums)
        nums_sum[0] = nums[0]
        for i in range(1, len(nums)):
            nums_sum[i] = nums_sum[i-1] + nums[i]

        while low < high:
            mid = (low + high) // 2
            if self.can_split(nums_sum, m, mid):
                high = mid
            else:
                low = mid + 1
        return low

'''Test cases

[7,2,5,10,8]\n1


'''
        
# @lc code=end

