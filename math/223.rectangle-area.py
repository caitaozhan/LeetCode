#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        
        overlap = -1
        if bx1 >= ax2 or ax1 >= bx2 or by1 >= ay2 or ay1 >= by2:
            overlap = 0
        else:
            xlist = sorted([ax1, ax2, bx1, bx2])
            ylist = sorted([ay1, ay2, by1, by2])
            x1, x2 = xlist[1], xlist[2]
            y1, y2 = ylist[1], ylist[2]
            overlap = (x2 - x1) * (y2 - y1)

        return area1 + area2 - overlap
            
# @lc code=end

