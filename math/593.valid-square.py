#
# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#
# https://leetcode.com/problems/valid-square/description/
#
# algorithms
# Medium (42.68%)
# Likes:    273
# Dislikes: 439
# Total Accepted:    37K
# Total Submissions: 85.7K
# Testcase Example:  '[0,0]\n[1,1]\n[1,0]\n[0,1]'
#
# Given the coordinates of four points in 2D space, return whether the four
# points could construct a square.
# 
# The coordinate (x,y) of a point is represented by an integer array with two
# integers.
# 
# Example:
# 
# 
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
# 
# 
# 
# 
# Note:
# 
# 
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal
# angles (90-degree angles).
# Input points have no order.
# 
# 
# 
# 
#

from typing import List
import math

# @lc code=start
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dist = []
        dist.append(self.distance(p1, p2))
        dist.append(self.distance(p1, p3))
        dist.append(self.distance(p1, p4))
        dist.append(self.distance(p2, p3))
        dist.append(self.distance(p2, p4))
        dist.append(self.distance(p3, p4))
        dist.sort()
        eps = 1e-10
        if dist[0] > 0 and dist[0] == dist[1] == dist[2] == dist[3] and dist[4] == dist[5] and abs(math.sqrt(2)*dist[0] - dist[4]) < eps:
            return True
        else:
            return False
    
    def distance(self, p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# @lc code=end

