#
# @lc app=leetcode id=252 lang=python3
#
# [252] meeting rooms
#

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key = lambda x: x[1])
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < right:
                return False
            else:
                right = intervals[i][1]
        return True


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True


