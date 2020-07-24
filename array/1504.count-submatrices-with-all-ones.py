'''
Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

Example 1:

Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.

Example 2:

Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
Example 3:

Input: mat = [[1,1,1,1,1,1]]
Output: 21
Example 4:

Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
Output: 5

'''

from typing import List

class Solution:
    def count(self, num):
        return int((num+1)*num/2)
    
    def one_row(self, row):
        ''' solve the proble for one row
        '''
        row.append(0)
        total = 0
        ones = 0
        for i in row:
            if i == 1:
                ones += 1
            else:
                total += self.count(ones)
                ones = 0
        return total
        
    def collapse(self, mat, i, j):
        size = len(mat[i])
        row = []
        for k in range(size):
            zero = False
            for l in range(i, j+1):
                if mat[l][k] == 0:
                    zero = True
                    break
            if zero:
                row.append(0)
            else:
                row.append(1)
        return row
        
    def numSubmat(self, mat: List[List[int]]) -> int:
        # step 1: one row
        ans = 0
        for row in mat:
            ans += self.one_row(row)
        
        # step 2: multiple rows from collapse
        for i in range(len(mat)):
            for j in range(i+1, len(mat)):
                row = self.collapse(mat, i, j)
                ans += self.one_row(row)
        
        return ans
