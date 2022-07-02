#
# @lc app=leetcode id=1465 lang=python3
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#

from typing import List

# @lc code=start
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0, h])
        verticalCuts.extend([0, w])
        horizontalCuts.sort()
        verticalCuts.sort()
        h_max, v_max = 0, 0
        for i in range(1, len(horizontalCuts)):
            h_max = max(h_max, horizontalCuts[i] - horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            v_max = max(v_max, verticalCuts[i] - verticalCuts[i-1])
        return (h_max * v_max) % (10**9 + 7)

# @lc code=end

