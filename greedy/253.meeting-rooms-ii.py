"""

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

"""

import heapq
from typing import List

class Solution:
    '''greedy 1: sort the intervals by the ending time
       greedy 2: when there are multiple rooms available, choose the one with the maximum ending time
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[1])
        rooms = []
        for s, e in intervals:
            exist = False
            max_end = -1
            indx    = -1
            for i in range(len(rooms)):
                if rooms[i] <= s:
                    if rooms[i] > max_end:
                        max_end = rooms[i]
                        indx = i
                    exist = True
            if exist:
                rooms[indx] = e
            else:
                rooms.append(e)
        return len(rooms)


class Solution2:
    '''the 'symmetry' version of the first Solution
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        rooms = []
        for s, e in intervals:
            exist = False
            min_end = float('inf')
            indx    = -1
            for i in range(len(rooms)):
                if rooms[i] <= s:
                    if rooms[i] < min_end:
                        min_end = rooms[i]
                        indx = i
                    exist = True
            if exist:
                rooms[indx] = e
            else:
                rooms.append(e)
        return len(rooms)


class Solution3:
    '''improve Solution2 using a heap
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x:x[0])
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        for s, e in intervals[1:]:
            if rooms[0] <= s:         # room available
                heapq.heappop(rooms)
            heapq.heappush(rooms, e)
        return len(rooms)


class Solution4:
    '''if multiple confernence rooms are available, put in any of them.
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        rooms = []                # end time
        for s, e in intervals:
            for i in range(len(rooms)):
                if rooms[i] <= s:
                    rooms[i] = e
                    break
            else:
                rooms.append(e)
        return len(rooms)

'''
[[0,30],[5,10],[15,20]]
[[7,10],[2,4]]
[[13,15],[1,13]]
[[2,15],[36,45],[9,29],[16,23],[4,9]]
'''