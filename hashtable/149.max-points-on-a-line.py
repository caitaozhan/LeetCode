#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    '''O(n^2), two points form a line, charecterized by two coefficients.
       So a line is hashed into two coefficients. naturally use a defaultdict(set)
    '''
    def maxPoints(self, points: List[List[int]]) -> int:
        d1 = defaultdict(set)  # for y = ax + b, (a, b) -> {point1, point2, ...}
        d2 = defaultdict(set)  # for x = c       c -> {point1, point2}
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i):
                x2, y2 = points[j]
                if x1 != x2:
                    a = (y2 - y1) / (x2 - x1)
                    b = y1 - a*x1
                    d1[(a, b)].add((x1, y1))
                    d1[(a, b)].add((x2, y2))
                else:
                    d2[x1].add((x1, y1))
                    d2[x1].add((x2, y2))
        ans = 1                       # BUG: corner case is that len(points) == 1
        for key, val in d1.items():
            ans = max(ans, len(val))
        for key, val in d2.items():
            ans = max(ans, len(val))
        return ans




        
# @lc code=end

