"""

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:



Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
Example 3:

Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4
Example 4:

Input: points = [[-1000000,-1000000],[1000000,1000000]]
Output: 4000000
Example 5:

Input: points = [[0,0]]
Output: 0
 

Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.



"""

from typing import List

class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        while self.parent[x] != x:
            x_p = self.parent[x]
            self.parent[x] = self.parent[x_p]  # path compression
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        x_p = self.find(x)
        y_p = self.find(y)
        if x_p != y_p:   # not in the same joint set
            self.parent[x_p] = y_p    # parent of y is the new root


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(len(points)):
                dist = self.distance(points[i], points[j])
                edges.append((dist, i, j))
        edges = sorted(edges, key=lambda x:x[0])
        
        ans = 0
        n = len(points)
        dsu = DSU(n)
        i = 0
        j = 0 # inter through the edges
        while i < n-1:  # MST algo.
            dist, a, b = edges[j]
            a_p = dsu.find(a)
            b_p = dsu.find(b)
            if a_p != b_p:
                dsu.union(a, b)
                i += 1
                ans += dist
            j += 1
        return ans
                
    def distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
