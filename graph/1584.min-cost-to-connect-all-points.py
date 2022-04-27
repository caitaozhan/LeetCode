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

class DS:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(self.n)]
    
    def find(self, x):
        while x != self.parent[x]:
            x_p = self.parent[x]
            self.parent[x] = self.parent[x_p]  # path compression
            x = x_p
        return x
    
    def union(self, x, y):
        x_p = self.find(x)
        y_p = self.find(y)
        if x_p != y_p:
            self.parent[y_p] = x_p  # parent of x is the new root
        

class Solution:
    
    def distance(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # step 1: sort all the edges
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):   # start from i+1, not 0. remove duplicates
                dist = self.distance(points[i], points[j])
                edges.append((dist, i, j))
        edges.sort(key=lambda x: x[0])
        
        # step 2: iterate the edges
        i = 0  # for successfully added edges
        j = 0  # for all edges
        ans = 0
        ds = DS(n)
        while i < n - 1:
            dist, x, y = edges[j]
            x_p = ds.find(x)
            y_p = ds.find(y)
            if x_p != y_p:
                ds.union(x, y)
                ans += dist
                i += 1
            j += 1
        return ans