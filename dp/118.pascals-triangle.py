#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or i == j:
                    row.append(1)
                else:
                    row.append(ans[i-1][j-1] + ans[i-1][j])
            ans.append(row)
        return ans
        
# @lc code=end

