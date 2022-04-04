#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        # step 1: find the first decrease at [i]
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        
        if i != -1:
            # step 2.1: find the first largest element in [i+1:] at [j]
            j = len(nums) - 1
            while j > i:
                if nums[j] > nums[i]:
                    break
                j -= 1
            # step 2.2: swap [i] and [j]
            nums[i], nums[j] = nums[j], nums[i]

        # step 3: reverse [i+1:]
        left = i+1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        



        
# @lc code=end

