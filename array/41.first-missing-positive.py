#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

from typing import List

# @lc code=start
class Solution:
    '''the index i equals to the value [i]
    '''
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        # in-place change, to get [1, 2, 3, 4, ...]
        while i < n:
            if nums[i] == i + 1:                 # already satisfy [1, 2, 3, 4, ...]
                i += 1
            else:
                if nums[i] < 1 or nums[i] > n:   # ignore out of bound
                    i += 1
                else:
                    # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]  # this swapping won't work
                    num = nums[i]
                    if nums[i] == nums[num - 1]: # no need to swap, and prevent endless useless swapping
                        i += 1
                    else:
                        nums[i], nums[num - 1] = nums[num - 1], nums[i]

        i = 0
        while i < n and nums[i] == i + 1:
            i += 1
        return i + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # check if 1 is present
        if 1 not in nums:
            return 1

        # replace negative numbers, zero, and larger than n numbers by 1 (kind of a trick)
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 1
        
        # use abs(num) as index, negative means existance
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1

        # find the first positive number
        i = 0
        while i < n and nums[i] < 0:
            i += 1
        return i + 1

# nums = [1, 2, 0]
nums = [3, 4, -1, 1]
# nums = [7,8,9,11,12]
# nums = [1]

s = Solution()
print(s.firstMissingPositive(nums))
            
        
# @lc code=end

