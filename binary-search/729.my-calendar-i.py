#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#


# @lc code=start
class MyCalendar:
    '''store the intervals in an ordered list
       search is O(logn), but insertion is O(n)
    '''
    def __init__(self):
        self.calendar = []
    
    def bisect_left(self, target):
        low = 0
        high = len(self.calendar)
        while low < high:
            mid = (low + high) // 2
            if self.calendar[mid][0] < target:
                low = mid + 1
            else:
                high = mid
        return low

    def book(self, start: int, end: int) -> bool:
        # binary search
        index = self.bisect_left(start)
        # check left interval
        if 0 <= index - 1 < len(self.calendar):
            if self.calendar[index - 1][1] > start:
                return False
        # check right interval
        if 0 <= index < len(self.calendar):
            if self.calendar[index][0] < end:
                return False
        # now it is fine to book
        self.calendar.insert(index, [start ,end])
        return True
        
from sortedcontainers import SortedList
        
class MyCalendar:
    '''store the intervals in an ordered list by a package sortedcontainers
       search is O(logn), insertion is also O(logn)
    '''
    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        # binary search
        index = self.calendar.bisect_left(start)
        # check left interval
        if 0 <= index - 1 < len(self.calendar):
            if self.calendar[index - 1][1] > start:
                return False
        # check right interval
        if 0 <= index < len(self.calendar):
            if self.calendar[index][0] < end:
                return False
        # now it is fine to book
        self.calendar.add((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

