#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
from heapq import heappush, heappop
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for n, c in count.items():
            heappush(heap, (c, n))
            if len(heap) > k:
                heappop(heap)
        return [n for _, n in heap]
        
# @lc code=end

