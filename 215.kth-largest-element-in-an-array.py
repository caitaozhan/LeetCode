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

class Solution:
    '''use the min heap
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        nums = [-i for i in nums]  # find the kth smallest
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)

# @lc code=end

