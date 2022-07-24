#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

from typing import List

# @lc code=start
class Solution:
    '''a straight-forward binary search based solution, O(nlogn)
       but it didn't utilize one condition of the problem: the elements are sorted from top-down
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_serach(i, target):
            low = 0
            high = len(matrix[i]) - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False
        
        m = len(matrix)
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1]:
                if binary_serach(i, target):
                    return True
        return False


class Solution:
    '''a clever O(n + m) searching solution that utilize all the conditions
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        cur = [m-1, 0]
        while 0 <= cur[0] < m and 0 <= cur[1] < n:
            if matrix[cur[0]][cur[1]] > target:
                cur[0] -= 1
            elif matrix[cur[0]][cur[1]] < target:
                cur[1] += 1
            else:
                return True
        return False
            

# @lc code=end

