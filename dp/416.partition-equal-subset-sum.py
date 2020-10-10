#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (43.21%)
# Likes:    3157
# Dislikes: 74
# Total Accepted:    209.1K
# Total Submissions: 474.2K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
# 
# Note:
# 
# 
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 == 1:
            return False
        dp = [[False for _ in range(summ//2+1)] for _ in range(len(nums))]
        dp[0][0] = True
        for i in range(0, len(nums)):
            for j in range(summ//2+1):
                if i == 0:
                    if j == nums[i]:
                        dp[i][j] = True
                elif dp[i-1][j] or (j>=nums[i] and dp[i-1][j-nums[i]]):
                    dp[i][j] = True
        return dp[len(nums)-1][summ//2]


class SolutionTLE:
    '''a solution by constructing the subsets
    '''
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()        # first utilize the larger elements
        target, rem = divmod(sum(nums), 2)
        if rem!=0:
            return False
        groups= [0,0]

        def search(groups):
            if not nums:
                return True
            ele = nums.pop()
            for i, group in enumerate(groups):
                if group+ele <= target:
                    groups[i] += ele
                    if search(groups):
                        return True
                    groups[i] -= ele
                if not group:
                    break
            nums.append(ele)
            return False
        
        return search(groups)

def test():
    nums = [10,4,2,5,3,2,2,2,2]
    s = Solution()
    print(s.canPartition(nums))

test()

# @lc code=end

