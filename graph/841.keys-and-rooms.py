#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    '''dfs, O(n)
    '''
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        g = defaultdict(list)
        for cur, nxt_list in enumerate(rooms):
            for nxt in nxt_list:
                g[cur].append(nxt)
        
        def dfs(cur: int):
            if len(self.visited) == n:
                self.visited_all = True
                return
            for nxt in g[cur]:
                if nxt not in self.visited:
                    self.visited.add(nxt)
                    dfs(nxt)

        start = 0
        self.visited = set([start])
        self.visited_all = False
        dfs(start)
        if self.visited_all == True:
            return True
        else:
            return False


class Solution:
    '''there is no need for a defaultdict............
       the rooms itself is a defaultdict
    '''
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = set([0])
        while stack:
            cur = stack.pop()
            for nxt in rooms[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    stack.append(nxt)
        return len(visited) == len(rooms)


rooms = [[1],[2],[3],[]]
rooms = [[1],[],[0,3],[1]]
s = Solution()
print(s.canVisitAllRooms(rooms))

# @lc code=end

