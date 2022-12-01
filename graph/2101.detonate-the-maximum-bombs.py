'''

You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. 
This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. 
xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, 
whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. 
When a bomb is detonated, it will detonate all bombs that lie in its range. 
These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

'''

import math
from collections import defaultdict
from typing import List


class Solution:
    '''O(n^2), bfs at each node
    '''
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def distance(bomb1, bomb2):
            return math.sqrt((bomb1[0] - bomb2[0]) ** 2 + (bomb1[1] - bomb2[1]) ** 2)

        def bfs(start):
            count = 1
            queue = [start]
            visited = set(queue)
            while queue:
                new_queue = []
                for node in queue:
                    for nxt in g[node]:
                        if nxt not in visited:
                            visited.add(nxt)
                            count += 1
                            new_queue.append(nxt)
                queue = new_queue
            return count

        # step 1: build the directed graph
        g = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(i+1, n):
                bomb1 = bombs[i]
                bomb2 = bombs[j]
                dist = distance(bomb1, bomb2)
                if bomb1[2] >= dist:
                    g[i].append(j)
                if bomb2[2] >= dist:
                    g[j].append(i)
        
        # step 2: do a bfs at each node
        ans = 0
        for i in range(n):
            num = bfs(i)
            ans = max(num, ans)
        return ans


bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
s = Solution()
print(s.maximumDetonation(bombs))
