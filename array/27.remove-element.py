#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

from typing import List

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            while i < j and nums[i] != val:
                i += 1
            while j > i and nums[j] == val:
                j -= 1
            # now nums[i] == val and nums[j] != val
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        return i

        
# @lc code=end

