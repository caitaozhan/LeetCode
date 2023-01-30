#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (33.18%)
# Likes:    1902
# Dislikes: 194
# Total Accepted:    272.2K
# Total Submissions: 803.1K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
from typing import List
from bisect import bisect_left, bisect_right, insort_left

class Solution:
    '''O(n), Sep 13, 2020
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals

        start = [a for a, _ in intervals]
        left = bisect_left(start, newInterval[0])
        right = bisect_right(start, newInterval[1])
        left = left - 1 if left > 0 else 0
        ans = intervals[:left]
        middle = self.get_middle(intervals, newInterval, left, right)
        ans.extend(middle)
        ans.extend(intervals[right:])
        return ans

    def get_middle(self, intervals, newInterval, left, right):
        middle = []
        if newInterval[0] > intervals[left][1]:
            middle.append(intervals[left])   # left side
            if newInterval[1] < intervals[right-1][1]:
                middle.append([newInterval[0], intervals[right-1][1]])
            else:
                middle.append([newInterval[0], newInterval[1]])
        else:
            right1 = right-1 if right>0 else 0
            if newInterval[1] < intervals[right1][0]:
                middle.append(newInterval)
            else:
                if newInterval[1] < intervals[right1][1]:
                    middle.append([min(newInterval[0], intervals[left][0]), intervals[right1][1]])
                else:
                    middle.append([min(newInterval[0], intervals[left][0]), newInterval[1]])
        return middle



class Solution:
    '''O(n), Jan 15, 2023
       using insort_left that modify the input array
       then build the ans array in a smart way, by using ans[-1][1] as the threshold
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insort_left(intervals, newInterval)
        n = len(intervals)
        ans = []
        i = 0
        for i in range(n):
            if len(ans) == 0 or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                if intervals[i][1] > ans[-1][1]:
                    ans[-1][1] = intervals[i][1]
        return ans



intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
# intervals = [[5,7]]
# newInterval = []
s = Solution()
print(s.insert(intervals, newInterval))
   


# @lc code=end

