#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    '''O(nlogn) dummy solution
    '''
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        i = 0
        while i < len(nums):
            if nums_sorted[i] != nums[i]:
                break
            i += 1
        j = len(nums) - 1
        while j >= 0:
            if nums_sorted[j] != nums[j]:
                break
            j -= 1
        if i == len(nums):
            return 0
        else:
            return j - i + 1


class Solution:
    '''O(n) solution with two pass monotone stack
    '''
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        istack = []   # increasing stack
        left = float('inf')
        for i in range(len(nums)):
            while istack and nums[istack[-1]] > nums[i]:
                left = min(left, istack.pop())
            istack.append(i)
        
        dstack = []   # decreasing stack
        right = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            while dstack and nums[dstack[-1]] < nums[i]:
                right = max(right, dstack.pop())
            dstack.append(i)
        
        if left == float('inf'):
            return 0
        else:
            return right - left + 1

# @lc code=end

