#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # step 1: find the row
        if target < matrix[0][0]:
            return False
        row_index = 0
        while row_index < m:
            if target <= matrix[row_index][-1]:
                break
            row_index += 1
        if row_index == m:
            return False
        
        # step 2: binary search in the row
        nums = matrix[row_index]
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False



# @lc code=end

