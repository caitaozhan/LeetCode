#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

from collections import defaultdict
from typing import List


class Solution:
    '''the key is to start at the ocean, instead of the cell, i.e., think reversely
       do BFS two times, one for pacific and one for atlantic
       O(nm) where n, m is the length, width of the grid
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(queue: list, visited: set, ocean: str):
            while len(queue) > 0:
                new_queue = []
                for cur in queue:
                    for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        nxt = (cur[0] + x, cur[1] + y)
                        if (0 <= nxt[0] < self.m) and (0 <= nxt[1] < self.n) and (nxt not in visited):
                            if heights[nxt[0]][nxt[1]] >= heights[cur[0]][cur[1]]:  # going to higher places
                                new_queue.append(nxt)
                                visited.add(nxt)
                                reachable[nxt].add(ocean)
                queue = new_queue

        reachable = defaultdict(set)
        self.m = len(heights)
        self.n = len(heights[0])
        # BFS for pacific
        ocean = 'p'
        queue = []
        visited = set()
        for i in range(self.m):
            node = (i, 0)
            queue.append(node)
            visited.add(node)
            reachable[node].add(ocean)
        for j in range(1, self.n):
            node = (0, j)
            queue.append(node)
            visited.add(node)
            reachable[node].add(ocean)
        bfs(queue, visited, ocean)

        # BFS for atlantic
        ocean = 'a'
        queue = []
        visited = set()
        for i in range(self.m):
            node = (i, self.n - 1)
            queue.append(node)
            visited.add(node)
            reachable[node].add(ocean)
        for j in range(self.n):
            node = (self.m - 1, j)
            queue.append(node)
            visited.add(node)
            reachable[node].add(ocean)
        bfs(queue, visited, ocean)

        # get the answer
        ans = []
        for i in range(self.m):
            for j in range(self.n):
                node = (i, j)
                if len(reachable[node]) == 2:
                    ans.append([i, j])
        return ans

# @lc code=end

