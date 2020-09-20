"""

You are given a rows x cols matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (rows - 1, cols - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative return -1.

Notice that the modulo is performed after getting the maximum product.

 

Example 1:

Input: grid = [[-1,-2,-3],
               [-2,-3,-3],
               [-3,-3,-2]]
Output: -1
Explanation: It's not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
Example 2:

Input: grid = [[1,-2,1],
               [1,-2,1],
               [3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is in bold (1 * 1 * -2 * -4 * 1 = 8).
Example 3:

Input: grid = [[1, 3],
               [0,-4]]
Output: 0
Explanation: Maximum non-negative product is in bold (1 * 0 * -4 = 0).
Example 4:

Input: grid = [[ 1, 4,4,0],
               [-2, 0,0,1],
               [ 1,-1,1,1]]
Output: 2
Explanation: Maximum non-negative product is in bold (1 * -2 * 1 * -1 * 1 * 1 = 2).
 

Constraints:

1 <= rows, cols <= 15
-4 <= grid[i][j] <= 4

"""

from typing import List

class Solution:
    '''refer to 152. maximum product subarray, the key is to have two dp arrays, on for max product and one for min product
    '''
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        x_len = len(grid)
        y_len = len(grid[0])
        dp_max = [[0 for _ in range(y_len)] for _ in range(x_len)]
        dp_min = [[0 for _ in range(y_len)] for _ in range(x_len)]
        for i in range(x_len):
            for j in range(y_len):
                if grid[i][j] == 0:
                    dp_max[i][j] = 0
                    dp_min[i][j] = 0
                    continue

                if i == 0 and j == 0:
                    dp_max[i][j] = grid[i][j]
                    dp_min[i][j] = grid[i][j]
                elif i == 0:
                    dp_max[i][j] = max(grid[i][j]*dp_max[i][j-1], grid[i][j]*dp_min[i][j-1])
                    dp_min[i][j] = min(grid[i][j]*dp_max[i][j-1], grid[i][j]*dp_min[i][j-1])
                elif j == 0:
                    dp_max[i][j] = max(grid[i][j]*dp_max[i-1][j], grid[i][j]*dp_min[i-1][j])
                    dp_min[i][j] = min(grid[i][j]*dp_max[i-1][j], grid[i][j]*dp_min[i-1][j])
                else:
                    dp_max[i][j] = max(grid[i][j]*dp_max[i-1][j], grid[i][j]*dp_min[i-1][j], grid[i][j]*dp_max[i][j-1], grid[i][j]*dp_min[i][j-1])
                    dp_min[i][j] = min(grid[i][j]*dp_max[i-1][j], grid[i][j]*dp_min[i-1][j], grid[i][j]*dp_max[i][j-1], grid[i][j]*dp_min[i][j-1])
        return dp_max[-1][-1] % MOD if dp_max[-1][-1] >= 0 else -1
