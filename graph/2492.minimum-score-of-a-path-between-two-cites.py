'''

You are given a positive integer n representing n cities numbered from 1 to n. 
You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that 
there is a bidirectional road between cities ai and bi with a distance equal to distancei. 
The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, 
and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.

'''


class Solution:
    '''just do a bfs, and record the minimum road during the bfs
    '''
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b, dist in roads:
            g[a].append((b, dist))
            g[b].append((a, dist))
        ans = float('inf')
        queue = [1]
        visited = set()
        while queue:
            new_queue = []
            for node in queue:
                for nxt, dist in g[node]:
                    ans = min(ans, dist)
                    if nxt not in visited:
                        new_queue.append(nxt)
                        visited.add(nxt)
            queue = new_queue
        return ans
