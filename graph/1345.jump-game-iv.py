#
# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#

from collections import defaultdict
from typing import List

# @lc code=start
class Solution:
    '''build graph and do BFS
       O(V + E), TLE
       time=348s for a len(arr)=50000 sample with almost the same number
    '''
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        # step 1: build graph
        mydict = defaultdict(list)
        for i, num in enumerate(arr):
            mydict[num].append(i)

        n = len(arr)
        g = defaultdict(list)  # graph
        for i in range(n):
            nxt = i + 1        # neighbors
            if nxt < n:
                g[i].append(nxt)
            nxt = i - 1
            if nxt >= 0:
                g[i].append(nxt)
        
        for _, reachable in mydict.items():
            for i in range(len(reachable)):
                for j in range(i + 1, len(reachable)):
                    node_a = reachable[i]
                    node_b = reachable[j]
                    if abs(node_a - node_b) != 1:    # not neighbors
                        g[node_a].append(node_b)
                        g[node_b].append(node_a)
        
        # step 2: do BFS
        visited = [0] * n
        start = 0
        queue = [start]
        visited[start] = 1   # it is visited when it is being put in the queue
        layers = 0
        while queue:
            layers += 1
            new_queue = []
            for cur in queue:
                for nxt in g[cur]:
                    if visited[nxt] == 1:
                        continue
                    if nxt == n - 1:
                        return layers

                    new_queue.append(nxt)
                    visited[cur] = 1
                
            queue = new_queue


class Solution:
    '''build graph and do BFS
       Don't build the real complete graph... just build a 'semi-graph'
       Save time building the complete graph, but still O(V + E)
       time=77s for a len(arr)=50000 sample with almost the same number
    '''
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        # step 1: build a "semi-graph"
        mydict = defaultdict(list)
        for i, num in enumerate(arr):
            mydict[num].append(i)
        
        # step 2: do BFS
        n = len(arr)
        visited = [0] * n
        start = 0
        queue = [start]
        visited[start] = 1   # it is visited when it is being put in the queue
        layers = 0
        while queue:
            layers += 1
            new_queue = []
            for cur in queue:
                # move left and right in the array
                for nxt in [cur - 1, cur + 1]:
                    if nxt < 0 or nxt >= n or visited[nxt] == 1:
                        continue
                    if nxt == n - 1:
                        return layers
                    new_queue.append(nxt)
                    visited[nxt] = 1

                # same number in the array
                neighbors = mydict[arr[cur]]
                for nxt in neighbors:
                    if nxt == cur or visited[nxt] == 1:
                        continue
                    if nxt == n - 1:
                        return layers
                    new_queue.append(nxt)
                    visited[nxt] = 1
                
            queue = new_queue


class Solution:
    '''build graph and do BFS
       Don't build the real complete graph... just build a 'semi-graph'
       time=0.05s for a len(arr)=50000 sample with almost the same number
    '''
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        # step 1: build a "semi-graph"
        mydict = defaultdict(list)
        for i, num in enumerate(arr):
            mydict[num].append(i)
        
        # step 2: do BFS
        n = len(arr)
        visited = [0] * n
        start = 0
        queue = [start]
        visited[start] = 1   # it is visited when it is being put in the queue
        layers = 0
        while queue:
            layers += 1
            new_queue = []
            for cur in queue:
                # move left and right in the array
                for nxt in [cur - 1, cur + 1]:
                    if nxt < 0 or nxt >= n or visited[nxt] == 1:
                        continue
                    if nxt == n - 1:
                        return layers
                    new_queue.append(nxt)
                    visited[nxt] = 1

                # same number in the array
                neighbors = mydict[arr[cur]]
                for nxt in neighbors:
                    if visited[nxt] == 1:
                        continue
                    if nxt == n - 1:
                        return layers
                    new_queue.append(nxt)
                    visited[nxt] = 1
                
                # don't let it jump to another same number again
                mydict[arr[cur]].clear()
                
            queue = new_queue


# arr = [100,-23,-23,404,100,23,23,23,23,23,23,23,23,23,3,5]

# arr = [7]* 50000 + [8, 11]
arr = [7,7,2,1,7,7,7,3,4,1]

print(len(arr))

s = Solution()
print(s.minJumps(arr))

        
# @lc code=end

