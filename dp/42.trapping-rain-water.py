#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (45.80%)
# Likes:    5126
# Dislikes: 94
# Total Accepted:    396.2K
# Total Submissions: 861.3K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#

from typing import List

# @lc code=start
class Solution2:
    '''DP solution
    input: x[0 ... n-1]
    subproblem-left: dp_left[i] is the largest number from [0 ... i-1]
    subproblem-right: dp_right[i] is the largest number from [i+1 ...]
    equation for left: dp_left[i] = max(dp_left[i-1], x[i])
    ans: the trapped water problem uses the above subproblems.
    '''
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        dp_left = [0 for _ in range(n)]
        dp_right = [0 for _ in range(n)]
        for i in range(1, n):
            dp_left[i] = max(dp_left[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            dp_right[i] = max(dp_right[i+1], height[i+1])
        water = 0
        for i in range(1, n-1):
            sea_level =  min(dp_left[i], dp_right[i])
            if sea_level > height[i]:
                water += (sea_level - height[i])
        return water


class Solution:
    '''Monotone stack solution, here it is a decreasing stack
    '''
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
        
        water = 0
        stack = []   # decreasing stack in terms of height[i]
        for j in range(0, n):   # j is the right bound
            while stack and height[j] > height[stack[-1]]:  # > and >= both works here
                bottom = stack.pop()
                if not stack:
                    break
                i = stack[-1]   # i is the left bound
                horizon_dist = j - i - 1
                sea_leval = min(height[i], height[j])
                water += (sea_leval - height[bottom]) * horizon_dist
            stack.append(j)
        return int(water)

# @lc code=end

