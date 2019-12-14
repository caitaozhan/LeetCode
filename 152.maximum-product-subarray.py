#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (30.42%)
# Likes:    2833
# Dislikes: 121
# Total Accepted:    265.2K
# Total Submissions: 870.6K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#

from typing import List

# @lc code=start
class Solution:
    ''' first i used one dp array but failed,
        then i figured out that two dp arrays are needed, but still failed,
        finally i figured out the correct defination of the two dp arrays
    subproblem-1: dp_max[i] is the max of product of x[..., i] that ends with i
    subproblem-2: dp_min[i] is the min of product of x[..., i] that ends with i
    testcases: [2,3,-2,4,-1]; [-2,0,-1]; [3,-1,4,3,-2]; [-2]; [2,-5,-2,-4,3]
    '''
    def maxProduct(self, nums: List[int]) -> int:
        nums.insert(0, 0)
        dp_max = [-2**63 for _ in range(len(nums))]
        dp_min = [2**63 for _ in range(len(nums))]
        maxx = -2*63
        for i in range(1, len(nums)):
            # update dp_max
            if nums[i] == 0:
                dp_max[i] = 0
            elif nums[i] > 0:
                if dp_max[i-1] > 0:
                    dp_max[i] = dp_max[i-1] * nums[i]
                else:
                    dp_max[i] = nums[i]
            else: # nums[i] < 0:
                if dp_min[i-1] < 0:
                    dp_max[i] = dp_min[i-1] * nums[i]
                else:
                    dp_max[i] = nums[i]
            
            # update dp_min
            if nums[i] == 0:
                dp_min[i] = 0
            elif nums[i] > 0:
                if dp_min[i-1] < 0:
                    dp_min[i] = dp_min[i-1] * nums[i]
                else:
                    dp_min[i] = nums[i]
            else: # nums[i] < 0
                if dp_max[i-1] > 0:
                    dp_min[i] = dp_max[i-1] * nums[i]
                else:
                    dp_min[i] = nums[i]

            maxx = max(maxx, dp_max[i])

        return  maxx
            
# @lc code=end

