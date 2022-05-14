#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

from collections import defaultdict
from heapq import heappush, heappop

# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n+1)
        graph = defaultdict(list)
        for a, b, w in times:
            graph[a].append((b, w))
        
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = []
        for node in range(1, n + 1):
            if node == k:
                heappush(heap, (0, node))
            else:
                heappush(heap, (float('inf'), node))
        
        while heap:
            d, node = heappop(heap)
            if dist[node] < d:   # node is already visited
                continue
            for neigh, w in graph[node]:
                if dist[node] + w < dist[neigh]:
                    dist[neigh] = dist[node] + w
                    heappush(heap, (dist[neigh], neigh))
        
        maxx = max(dist[1:])
        return maxx if maxx < float('inf') else -1

        
# @lc code=end

