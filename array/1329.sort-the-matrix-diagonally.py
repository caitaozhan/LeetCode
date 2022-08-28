#
# @lc app=leetcode id=1329 lang=python3
#
# [1329] Sort the Matrix Diagonally
#

from typing import List

# @lc code=start
class Solution:
    # use the inbuilt sort
    # assume m = n, then time complexity is O(n^2*logn)
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        heads = []
        for j in range(n-1, -1, -1):
            heads.append((0, j))
        for i in range(1, m):
            heads.append((i, 0))
        for head in heads:
            # construct the diagonal list and sort it
            mylist = []
            i, j = head
            while i < m and j < n:
                mylist.append(mat[i][j])
                i += 1
                j += 1
            mylist.sort()
            # update mat
            i, j = head
            k = 0
            while i < m and j < n:
                mat[i][j] = mylist[k]
                i += 1
                j += 1
                k += 1
        return mat
            
from collections import Counter

class Solution:
    # use the counting sort
    # assume m = n, then time complexity is O(n^2)
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def counting_sorted(nums: list):
            '''modify nums in-place
            '''
            counter = Counter(nums)
            indx = 0
            for key, val in sorted(counter.items()):
                for _ in range(val):
                    nums[indx] = key
                    indx += 1
    
        m = len(mat)
        n = len(mat[0])
        heads = []
        for j in range(n-1, -1, -1):
            heads.append((0, j))
        for i in range(1, m):
            heads.append((i, 0))
        for head in heads:
            # construct the diagonal list and sort it
            mylist = []
            i, j = head
            while i < m and j < n:
                mylist.append(mat[i][j])
                i += 1
                j += 1
            counting_sorted(mylist)
            # update mat
            i, j = head
            k = 0
            while i < m and j < n:
                mat[i][j] = mylist[k]
                i += 1
                j += 1
                k += 1
        return mat

        
# @lc code=end

