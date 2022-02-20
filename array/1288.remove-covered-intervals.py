#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#
# https://leetcode.com/problems/remove-covered-intervals/description/
#
# algorithms
# Medium (59.42%)
# Likes:    314
# Dislikes: 17
# Total Accepted:    21.6K
# Total Submissions: 37.4K
# Testcase Example:  '[[1,4],[3,6],[2,8]]'
#
# Given a list of intervals, remove all intervals that are covered by another
# interval in the list.
# 
# Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <=
# d.
# 
# After doing so, return the number of remaining intervals.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,4],[2,3]]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: intervals = [[0,10],[5,12]]
# Output: 2
# 
# 
# Example 4:
# 
# 
# Input: intervals = [[3,10],[4,10],[5,11]]
# Output: 2
# 
# 
# Example 5:
# 
# 
# Input: intervals = [[1,2],[1,4],[3,4]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# 0 <= intervals[i][0] < intervals[i][1] <= 10^5
# All the intervals are unique.
# 
#

# @lc code=start

from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    '''greedy
    '''
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        counter = 0
        latest_end = 0
        for _, end in intervals:
            if end > latest_end:
                counter += 1
                latest_end = end
        return counter

class Solution:
    '''greedy. after sorting, while iterating from left to right, 
       it is ensured that the previous intervals will have a smaller equal left boundary
       then only need to compare the right boundary. the key idea is to keep updating the latest right boundary
    '''
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        remove = 0
        latest_end = 0
        for _, end in intervals:
            if end > latest_end:
                lateset_end = end
            else:
                remove += 1
        return len(intervals) - remove


class KeyWrapper:
    def __init__(self, iterable, key):
        self.it = iterable
        self.key = key
    
    def __getitem__(self, i):
        return self.key(self.it[i])

    def __len__(self):
        return len(self.it)

class Solution2:
    '''bianary search based, slow solution
    '''
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = [[i, a, b] for i, (a, b) in enumerate(intervals)]
        arr_l = sorted(intervals, key=lambda x:x[1])
        arr_r = sorted(intervals, key=lambda x:x[2])
        remove = set()
        for i, left, right in intervals:
            left1 = bisect_left(KeyWrapper(arr_l, key=lambda x:x[1]), left)
            left2 = bisect_right(KeyWrapper(arr_l, key=lambda x:x[1]), right)
            right1 = bisect_left(KeyWrapper(arr_r, key=lambda x:x[2]), left)
            right2 = bisect_right(KeyWrapper(arr_r, key=lambda x:x[2]), right)
            tmp1 = set([arr_l[indx][0] for indx in range(left1, left2)])
            tmp2 = set([arr_r[indx][0] for indx in range(right1, right2)])
            tmp1 = tmp1.intersection(tmp2)
            tmp1.remove(i)
            remove = remove.union(tmp1)
        return len(intervals) - len(remove)

# @lc code=end

