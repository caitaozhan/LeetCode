#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

from typing import List

# @lc code=start
class Solution:
    '''two pointers left and right, then do swapping
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            while i < len(nums) and nums[i] != val:
                i += 1
            while j >= 0 and nums[j] == val:
                j -= 1
            # now nums[i] == val and nums[j] != val
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
        return i


class Solution:
    '''two pointers both start from left, one is "slow pointer" and the other is "fast pointer"
       the fast pointer points to non-val elements
       the slow pointer points the removed array
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0   # index for the removed array
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[j] = nums[i]
            j += 1
        return j

        
# @lc code=end

