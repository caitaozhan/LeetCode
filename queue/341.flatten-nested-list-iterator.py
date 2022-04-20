#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

from collections import deque

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.i = 0
        self.n = len(nestedList)
        self.queue = deque()

    def flatten(self, nested_list: list):
        if len(nested_list) == 0:
            return []
        if len(nested_list) == 1:
            if nested_list[0].isInteger():
                return [nested_list[0].getInteger()]
            else:
                return self.flatten(nested_list[0].getList())
        else:
            if nested_list[0].isInteger():
                return [nested_list[0].getInteger()] + self.flatten(nested_list[1:])
            else:
                return self.flatten(nested_list[0].getList()) + self.flatten(nested_list[1:])

    def add_i_queue(self):
        '''move to the next self.i, but no return'''
        if self.nestedList[self.i].isInteger():
            self.queue.append(self.nestedList[self.i].getInteger())
        else: # type is nestedlist
            flattened = self.flatten(self.nestedList[self.i].getList())
            for num in flattened:
                self.queue.append(num)
        self.i += 1
    
    def next(self) -> int:
        if len(self.queue) > 0:
            return self.queue.popleft()
        if self.i < self.n:
            self.add_i_queue()
            self.i += 1
            return self.queue.popleft()

    def hasNext(self) -> bool:
        if len(self.queue) > 0:
            return True
        while self.i < self.n:
            self.add_i_queue()
            self.i += 1
            if len(self.queue) > 0:
                return True
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

