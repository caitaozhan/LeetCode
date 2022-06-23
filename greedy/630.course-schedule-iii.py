#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#

from heapq import heappush, heappop

# @lc code=start
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])  # sort by the deadline
        cur_time = 0
        heap = []
        for duration, deadline in courses:
            if cur_time + duration <= deadline:
                cur_time += duration
                heappush(heap, [-duration, deadline])       # schedule this course
            else:
                if len(heap) == 0:
                    continue
                top = heap[0]
                largest_dur = -top[0]
                if largest_dur > duration:
                    cur_time -= (largest_dur - duration)
                    heappop(heap)                           # remove a previously scheduled course
                    heappush(heap, [-duration, deadline])   # schedule this course --> only make the solution better
        return len(heap)
        
# @lc code=end

