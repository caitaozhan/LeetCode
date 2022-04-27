#
# @lc app=leetcode id=1696 lang=python3
#
# [1696] Jump Game VI
#

# @lc code=start
class Solution:
    '''O(n^2), TLE
    '''
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = nums[0]
        maxx = float('-inf')
        for i in range(n):
            start = max(0, i - k)
            for j in range(start, i):
                dp[i] = max(dp[i], dp[j] + nums[i])
        return dp[-1]

from collections import deque

class Solution:
    '''O(n), sliding window maxima based solution
    '''
    def __init__(self):
        self.nums = None
        self.k = None

    def update_queue(self, queue, i, dp):
        if queue and queue[0] == i - self.k:          # remove outdated item (over k ago)
            queue.popleft()

        while queue and dp[queue[-1]] < dp[i]:  # decreasing queue
            queue.pop()
        
        queue.append(i)

    def maxResult(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = k
        n = len(nums)
        queue = deque()
        queue.append(0)   # index in the queue
        dp = [float('-inf')] * n
        dp[0] = nums[0]
        i = 1
        while i < n:
            maxx = dp[queue[0]]
            dp[i] = maxx + nums[i]
            self.update_queue(queue, i, dp)
            i += 1
        return dp[-1]

# @lc code=end

