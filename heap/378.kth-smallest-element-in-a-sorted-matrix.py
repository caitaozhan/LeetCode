#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

from heapq import heappush, heappop
from typing import List

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        start = (matrix[0][0], 0, 0)    # (m[row][column], row, column)
        matrix[0][0] = None             # bad practice, but doing it for less than O(n^2) memory
        queue = [start]                 # priority queue
        counter = 1
        while queue:
            node = heappop(queue)
            val, i, j = node
            if counter == k:
                return val
            counter += 1
            nxt_j = j + 1
            if nxt_j < n and matrix[i][nxt_j] is not None:
                heappush(queue, (matrix[i][nxt_j], i, nxt_j))
                matrix[i][nxt_j] = None
            nxt_i = i + 1
            if nxt_i < n and matrix[nxt_i][j] is not None:
                heappush(queue, (matrix[nxt_i][j], nxt_i, j))
                matrix[nxt_i][j] = None


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(len(matrix)):
            heappush(heap, (matrix[i][0], i, 0))
        counter = 0
        while True:
            node = heappop(heap)
            val, i, j = node
            counter += 1
            if counter == k:
                return val
            nxt_j = j + 1
            if nxt_j < n:
                heappush(heap, (matrix[i][nxt_j], i, nxt_j))
        






class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        mylist = []
        for i in range(len(matrix)):
            mylist.extend(matrix[i])
        mylist.sort()
        return mylist[k-1] 


matrix = [[1,6,9],[4,11,13],[5,13,15]]
k = 5
matrix = [[1,6,9],[4,11,13],[5,13,15]]
k = 6
matrix = [[0,0,0],[2,7,9],[7,8,11]]
k = 7
s = Solution()
print(s.kthSmallest(matrix, k))


        
# @lc code=end

