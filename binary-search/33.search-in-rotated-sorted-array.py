#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

from typing import List

# @lc code=start
class Solution:

    def findK(self, nums, low, high):
        '''O(logN): find the 'pivot' index k, nums[k] is the lowest point
        '''
        if low > high:
            return None
        mid = (low + high) // 2
        if mid == 0:  # the lowest point cannot be at the left most
            self.findK(nums, low+1, high)  # BUG here, in case nums[1] is the lowest point
        if mid == len(nums) - 1:           # BUG here, nums[-1] could be the lowest point
            return mid
        if nums[mid-1] > nums[mid] and nums[mid] < nums[mid+1]:
            return mid
        elif low == high:
            return None
        else:
            if nums[mid] < nums[high]:
                return self.findK(nums, low, mid-1)
            else:
                return self.findK(nums, mid+1, high)

    def findTarget(self, nums, low, high, target):
        '''find the target and return its index'''
        low = low
        high = high
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1

        k = self.findK(nums, 0, len(nums)-1)  # BUG here. The problem says possibly rotated...
        if k is None:
            return self.findTarget(nums, 0, len(nums)-1, target)
        else:
            index1 = self.findTarget(nums, 0, k-1, target)
            index2 = self.findTarget(nums, k, len(nums)-1, target)
            if index1 == -1 and index2 != -1:  # BUG here, the original version was self.findTarget return None
                return index2                  # it turns out that "0 or None" is None. I expect 0 ...
            elif index1 != -1 and index2 == -1:
                return index1
            else:
                return -1


class Solution:
    # time beats 98.4%
    def search(self, nums: List[int], target: int) -> int:
        '''a modified binary search
        '''
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] < nums[mid] < nums[high]:                  # the normal case
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            elif nums[mid] > nums[low] and nums[mid] > nums[high]:  # when [mid] is larger than both [low] and [high]
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < nums[low] and nums[mid] < nums[high]:  # when [mid] is smaller than both [low] and [high]
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:   # high - low <= 1
                if nums[high] == target:
                    return high
                break
        return -1



s = Solution()

# nums = [1,3,5]
# target = 3
# print(s.search(nums, target))

# nums = [4,5,6,7,0,1,2]
# target = 0
# print(s.search(nums, target))

# nums = [4,5,6,7,0,1,2]
# target = 3
# print(s.search(nums, target))

# nums = [3, 5, 1]
# target = 1
# print(s.search(nums, target))

# nums = [3, 5, 1]
# target = 3
# print(s.search(nums, target))

nums = [5,1,2,3,4]
target = 1
print(s.search(nums, target))

# @lc code=end
