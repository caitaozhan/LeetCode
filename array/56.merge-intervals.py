#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (43.02%)
# Likes:    9765
# Dislikes: 436
# Total Accepted:    1.1M
# Total Submissions: 2.5M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def helper(i, intervals):
            if intervals[i][1] >= intervals[i + 1][0] and intervals[i][1] <= intervals[i + 1][1]:
                intervals[i][1] = intervals[i + 1][1]
                intervals.remove(intervals[i + 1])
                return True
            if intervals[i][1] >= intervals[i + 1][0] and intervals[i][1] > intervals[i + 1][1]:
                intervals.remove(intervals[i + 1])
                return True
            else:
                return False
        
        intervals = sorted(intervals)
        i = 0
        while i < len(intervals) - 1:
            ret = helper(i, intervals)
            if ret is False:
                i += 1
            
        return intervals
        
# @lc code=end

