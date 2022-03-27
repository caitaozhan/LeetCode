#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        summary = []
        for i, row in enumerate(mat):
            summary.append((sum(row), i))
        
        summary.sort(key=lambda x: (x[0], x[1]))
        ans = [x[1] for x in summary[:k]]
        return ans

        
# @lc code=end

