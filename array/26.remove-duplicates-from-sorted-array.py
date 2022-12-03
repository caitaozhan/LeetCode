#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

from typing import List

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        cur_min = float('-inf')
        for j in range(n):
            if nums[j] > cur_min:
                nums[i] = nums[j]    # [j] is the new element
                cur_min = nums[i]
                i += 1
        return i
            

class Solution:
    '''
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        for j in range(1, n):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]    # [j] is the new element
                i += 1
        return i
        
# @lc code=end

