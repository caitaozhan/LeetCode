#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

from heapq import heapify, heappop, heappush

# @lc code=start
class KthLargest:
    ''' use a min heap, python heapq is a min heap
    '''
    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        while len(nums) > k:
            heappop(nums)
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

