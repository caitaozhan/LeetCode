#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    '''Subproblem: dp[i][j]: is the length of the longest increasing path ending at [i][j]
       Equation: dp[i][j] = max(dp[i'][j']) + 1, where [i'][j'] is a valid neighbor, 
                 i.e. 2D index is correct and the according matrix value is smaller.
       The order of processing the subproblems: we go from the 2D index whose value in the matrix 
       is the smallest to the 2D index whose value in the matrix is the largest, i.e. accending order.
    '''
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        subproblem = []
        for i in range(m):
            for j in range(n):
                subproblem.append((matrix[i][j], i, j))
        subproblem.sort()

        dp = [[1 for _ in range(n)] for _ in range(m)]
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ans = 1
        for val, i, j in subproblem:
            max_neigh = 0
            for d in direction:
                x = i + d[0]
                y = j + d[1]
                if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]:
                    max_neigh = max(max_neigh, dp[x][y])
            if max_neigh > 0:
                dp[i][j] = max_neigh + 1
                ans = max(ans, dp[i][j])
        
        return ans

        
# @lc code=end

