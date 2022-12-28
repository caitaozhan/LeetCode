#
# @lc app=leetcode id=1962 lang=python3
#
# [1962] Remove Stones to Minimize the Total
#

from tpying import List
from heapq import heappush, heappop, heapify
import math

# @lc code=start
class Solution:
    '''greedy, using a heap, O(nlogn)
    '''
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = [-p for p in piles]
        heapify(h)
        for _ in range(k):
            num = heappop(h)
            num = -num
            num = math.ceil(num / 2)
            heappush(h, -num)
        return -sum(h)

        
# @lc code=end

