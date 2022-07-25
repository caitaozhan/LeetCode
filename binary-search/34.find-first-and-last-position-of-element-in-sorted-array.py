#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

from typing import List
from bisect import bisect_left, bisect_right

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search_left(nums, target):
            '''return the index of the most left target (bisect_left)
            '''
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    high = mid
                else:
                    low = mid + 1
            return low

        def binary_search_right(nums, target):
            '''return the index of the most right target plus 1 (bisect_right)
            '''
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid
            return low

        left = binary_search_left(nums, target)
        right = binary_search_right(nums, target) - 1
        if left <= right:
            return left, right
        else:
            return -1, -1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect_left(nums, target)
        right = bisect_right(nums, target) - 1
        if left <= right:
            return left, right
        else:
            return -1, -1


# nums = [5,7,7,8,8,8,9,10]
# nums = [5,7,7,8,8,10]
# nums = [5,7,7,8,10]
# nums = [5,7,7,10,10,10,11]
nums = [1]
target = 8
s = Solution()
print(s.searchRange(nums, target))


# @lc code=end

