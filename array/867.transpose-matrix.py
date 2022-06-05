#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)    # m row
        n = len(matrix[0]) # n column
        ans = [[0 for _ in range(m)] for _ in range(n)]  # n row, m column
        for i in range(n):
            for j in range(m):
                ans[i][j] = matrix[j][i]
        return ans

        
# @lc code=end

