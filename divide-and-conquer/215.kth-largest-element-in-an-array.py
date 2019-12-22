#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (51.06%)
# Likes:    2657
# Dislikes: 201
# Total Accepted:    481.5K
# Total Submissions: 941.4K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#

from typing import List

# @lc code=start
class Solution2:
    '''a simple way
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        return heapq.nlargest(k, nums)[-1]

class Solution3:
    '''heapq is a min heap by default. 
       Surpricingly, there are some undocumented methods to create a max heap
       However, people on stackoverflow says it not recommended
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq._heapify_max(nums)
        for _ in range(k-1):
            heapq._heappop_max(nums)
        return heapq._heappop_max(nums)

class Solution4:
    '''use the min heap: O(N + k*logN)
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        nums = [-i for i in nums]  # find the kth smallest
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)

class Solution5:
    '''implement heapq.nlargest by myself: O(N*logk)
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)

class Solution6:
    '''sorting O(NlogN)
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums)-k]


class Solution7:
    '''quick select using partition: O(N)
    '''
    def partition(self, nums, left, right):
        ''' in-place alter nums and return the index of the pivot
            left -- int -- finding elements larger than pivot
            right -- int finding elements smaller or equal than pivot
        '''
        pivot = nums[left]    # [l] is the pivot
        i, j = left, right
        while i < j:
            while i <= right and nums[i] <= pivot:
                i += 1
            while j >= left and nums[j] > pivot:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]  # swap
        nums[left], nums[j] = nums[j], nums[left]          # put the pivot to the right spot
        return j
    
    def partition2(self, nums, left, right):
        '''Another way of doing partition where both two pointers start at left side
        '''
        pivot = nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[right], nums[i + 1] = nums[i + 1], nums[right]
        return i + 1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left, right = 0, len(nums) - 1
        while True:
            pivot_index = self.partition2(nums, left, right)
            if pivot_index == target:
                return nums[target]
            elif pivot_index < target:
                left = pivot_index + 1
            else:
                right = pivot_index - 1


class Solution:
    '''quick select using partition: O(N)
    '''
    def partition(self, nums, left, right):
        ''' in-place alter nums and return the index of the pivot
            left -- int -- finding elements larger than pivot
            right -- int finding elements smaller or equal than pivot
        '''
        pivot = nums[left]    # [l] is the pivot
        i, j = left, right
        while i < j:
            while i <= right and nums[i] <= pivot:
                i += 1
            while j >= left and nums[j] > pivot:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]  # swap
        nums[left], nums[j] = nums[j], nums[left]          # put the pivot to the right spot
        return j

    def quickselect(self, nums, left, right, target):
        '''quick select
        '''
        if left == right:       # termination condition
            return nums[left]
        pivot_index = self.partition(nums, left, right)
        if pivot_index == target:
            return nums[target]
        elif pivot_index < target:
            left = pivot_index + 1
            return self.quickselect(nums, left, right, target)
        else:
            right = pivot_index - 1
            return self.quickselect(nums, left, right, target)
        

    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        return self.quickselect(nums, 0, len(nums) - 1, target)


def test():
    nums = [3,2,1,5,6,4]
    nums = [-10,2,3,1,2,4,5,5,6]
    s = Solution()
    s.findKthLargest(nums, 2)


if __name__ == '__main__':
    # test()
    pass

# @lc code=end

