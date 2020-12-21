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
    '''O(m^3 n) algorithm, the version I implemented during the interview
       6000 ms, time beat 5%
    '''
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


class Solution2:
    '''O(m^2 n) algorithm, opmizating Solution
       1200 ms, time beat 9%
    '''
    def one_row(self, row):
        '''compute the number of sub-arrays in an one-dimension array
        Args:
            row -- list<int>
        Return:
            int
        '''
        count = 0
        summ = 0
        for e in row:
            if e == 1:
                count += 1
            else:
                count = 0
            summ += count
        return summ

    def collapse(self, collapsed, row):
        '''element-wise AND
        Args:
            collapsed -- list<int>
            row       -- list<int>
        Return:
            list<int>
        '''
        ans = []
        for a, b in zip(collapsed, row):
            ans.append(a & b)
        return ans

    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        ans = 0
        for i in range(m):
            collapsed = [1] * n
            for j in range(i, m):
                collapsed = self.collapse(collapsed, mat[j])
                ans += self.one_row(collapsed)
        return ans


class Solution3:
    '''O(m n) algorithm, using monotone stack
       244 ms, time beat 77%
    '''
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        #precipitate mat to histogram 
        for i in range(m):
            for j in range(n):
                if mat[i][j] and i > 0: 
                    mat[i][j] += mat[i-1][j] #histogram 
        # for row in mat:
        #     print(row)
        # print()

        ans = 0
        for i in range(m):
            stack = [] # mono-stack of indices of non-decreasing height
            count = 0
            for j in range(n):
                while stack and mat[i][stack[-1]] > mat[i][j]: 
                    right  = stack.pop()                          # start
                    left   = stack[-1] if stack else -1           # end
                    count -= (mat[i][right] - mat[i][j])*(right - left) #adjust to reflect lower height

                count += mat[i][j] # count submatrices bottom-right at (i, j)
                # print(count, end=' ')
                ans += count
                stack.append(j)
            # print()

        return ans


def test1():
    mat = [[1,0,1],
           [1,1,0],
           [1,1,0]]
    mat = [[0,1,1,0],
           [0,1,1,1],
           [1,1,1,0]]
    s = Solution()
    print(s.numSubmat(mat))


def test2():
    mat = [[1,0,1],
           [1,1,0],
           [1,1,0]]
    mat = [[0,1,1,0],
           [0,1,1,1],
           [1,1,1,0]]
    s = Solution2()
    print(s.numSubmat(mat))  


def test3():
    mat = [[1,0,1],
           [1,1,0],
           [1,1,0]]
    mat = [[0,1,1,0],
           [0,1,1,1],
           [1,1,1,0]]
    s = Solution3()
    print(s.numSubmat(mat))


if __name__ == '__main__':
    test1()
    test2()
    test3()
