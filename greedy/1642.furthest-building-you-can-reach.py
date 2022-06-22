#
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#

from typing import List
from heapq import heappush, heappop

# @lc code=start
class Solution:
    '''An interesting greedy approach
       The key is to use a ladder whenever possible at the beginning, 
       and later replace the 'least cost-efficient' ladder with bricks.
    '''
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladderheap = []
        i = 0
        while i < len(heights) - 1:
            delta = heights[i+1] - heights[i]
            if delta <= 0:           # no need for bricks or ladders
                i += 1
                continue
            if ladders > 0:          # at the beginning, use a ladder whenever possible
                heappush(ladderheap, delta)
                ladders -= 1
                i += 1
                continue
            if len(ladderheap) == 0: # use bricks
                if bricks >= delta:
                    bricks -= delta
                    i += 1
                    continue
                else:
                    break
            if ladderheap and delta <= ladderheap[0]:  # use bricks
                if bricks >= delta:
                    bricks -= delta
                    i += 1
                    continue
                else:
                    break
            if ladderheap and delta > ladderheap[0]:   # replace a previous ladder with bricks
                previousladder = heappop(ladderheap)
                if bricks >= previousladder:
                    bricks -= previousladder
                    heappush(ladderheap, delta)
                    i += 1
                else:
                    break
        return i

                    
        
# @lc code=end

