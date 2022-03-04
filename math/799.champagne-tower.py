#
# @lc app=leetcode id=799 lang=python3
#
# [799] Champagne Tower
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0 for _ in range(102)] for _ in range(102)]
        tower[0][0] = poured
        for i in range(query_row+1):
            for j in range(i+1):
                if tower[i][j] > 1:
                    overflow = tower[i][j] - 1
                    tower[i+1][j] += overflow / 2
                    tower[i+1][j+1] += overflow / 2
        return 1 if tower[query_row][query_glass] > 1 else tower[query_row][query_glass]
        
# @lc code=end

