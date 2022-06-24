#
# @lc app=leetcode id=1354 lang=python3
#
# [1354] Construct Target Array With Multiple Sums
#

from heapq import heappush, heappop, heapify
from typing import List

# @lc code=start
class Solution:
    '''thinking backwards
       use a heap
       O(n + logk*logn)
    '''
    def isPossible(self, target: List[int]) -> bool:
        heap = []
        heap = [(-num, i) for i, num in enumerate(target)]
        heapify(heap)

        summ = sum(target)
        while True:
            top = heappop(heap)
            largest, i = -top[0], top[1]
            if largest == 1:
                return True
            others = summ - largest
            if others > 0 and largest > others * 2:   # speed up the subtraction
                ratio = largest // others
                nxt = largest - others*(ratio-1)
            else:
                nxt = largest - others
            if nxt <= 0 or nxt >= largest:
                return False
            target[i] = nxt
            summ -= (largest - nxt)
            heappush(heap, (-nxt, i))


target = [3,5,9]
# target = [1,1,1,2]
# target = [8,5]
# target = [1,1000_000_000]
# target = [2]
s = Solution()
print(s.isPossible(target))


        
# @lc code=end

