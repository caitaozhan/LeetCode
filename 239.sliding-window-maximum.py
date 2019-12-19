#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (40.09%)
# Likes:    2361
# Dislikes: 139
# Total Accepted:    206.8K
# Total Submissions: 514.6K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
# 
# Example:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 
# 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
# array.
# 
# Follow up:
# Could you solve it in linear time?
#

from typing import List

# @lc code=start
class Solution:

    def __init__(self):
        self.nums = []
        self.k = 0

    def init(self, nums, k):
        self.nums = nums
        self.k    = k

    def update_queue(self, queue, i):
        '''1. make sure the queue only contains past k elements (the sliding window)
           2. also make sure that queue[0] is the max element
        Args:
            queue -- collections.deque
            i     -- int -- index of self.nums at each iteration
        
        Test case:
        [4,3,2,1,0,-1,0,1,2]\n4
        '''
        if queue and queue[0] == i - self.k:                   # 1.
            queue.popleft()
        
        while queue and self.nums[queue[-1]] < self.nums[i]:   # 2.
            queue.pop()


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        self.init(nums, k)
        from collections import deque
        if not nums:
            return []

        queue = deque()   # a queue of nums's index
        output = []
        for i in range(k):
            self.update_queue(queue, i)
            queue.append(i)
        output.append(nums[queue[0]])
 
        for i in range(k, len(nums)):
            self.update_queue(queue, i)
            queue.append(i)
            output.append(nums[queue[0]])

        return output


# @lc code=end

