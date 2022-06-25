#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#

from typing import List

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modify = False
        i = 1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                break
            i += 1
        if i == len(nums):
            return True
        i_copy = i

        if i < 2 or nums[i-2] <= nums[i]:
            i = i_copy + 1         # choice 1: modify [i-1] smaller to [i], doable only under above conditions
            while i < len(nums):
                if nums[i] < nums[i-1]:
                    break
                i += 1
            if i == len(nums):
                return True

        i = i_copy
        nums[i] = nums[i-1]        # choice 2: modify [i] bigger to [i-1]
        i += 1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                break
            i += 1
        if i == len(nums):
            return True

        return False



class Solution:
    '''a succinct version of the above correct code
    '''
    def checkPossibility(self, nums: List[int]) -> bool:
        modify = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if modify == True:
                    return False
                else:
                    if i < 2 or nums[i-2] <= nums[i]:
                        nums[i-1] = nums[i]
                    else:
                        nums[i] = nums[i-1]
                    modify = True
        return True



nums = [4,2,1]
nums = [1,2,3,4,5,6,7,8,4,5]
s = Solution()
print(s.checkPossibility(nums))

# @lc code=end

