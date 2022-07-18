#
# @lc app=leetcode id=1074 lang=python3
#
# [1074] Number of Submatrices That Sum to Target
#

from typing import List
from collections import Counter, defaultdict

# @lc code=start
class Solution:
    '''the key is to associate with problem #560: https://leetcode.com/problems/subarray-sum-equals-k/
       reduce O(m^2 n^2) to O(m^2 n)
    '''
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        def dp_help(i, j):
            if i == -1 or j == -1:
                return 0
            return dp[i][j]

        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]   # dp[i][j] is the sum of matrix[0...i][0...j]
        dp[0][0] = matrix[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + matrix[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + matrix[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j]
        
        ans = 0
        for i1 in range(m):
            for i2 in range(i1, m):
                # reducing O(n^2) to O(n) by construting a "prefixsum hashtable"
                counter = Counter()
                counter[0] = 1
                for j in range(n):
                    two_sum = dp_help(i2, j) - dp_help(i1-1, j)
                    other = two_sum - target
                    ans += counter[other]   # if other is not in counter, then add 0 to ans
                    counter[two_sum] += 1
        return ans


class Solution:
    '''the dp_help() function has overhead, let's use a little larger dp array to prevent the dp_help() function
    '''
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]   # dp[i][j] is the sum of matrix[0...i-1][0...j-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i-1][j-1]
        
        ans = 0
        for i1 in range(1, m+1):
            for i2 in range(i1, m+1):
                # reducing O(n^2) to O(n) by construting a "prefixsum hashtable"
                counter = Counter()
                counter[0] = 1              # for the case when two_sum == target
                for j in range(1, n+1):
                    two_sum = dp[i2][j] - dp[i1-1][j]
                    other = two_sum - target
                    ans += counter[other]   # add the count of subarrays from [0...0] to [0...j-1] whose sum equals to other
                    counter[two_sum] += 1
        return ans


matrix = [[0,1,0],[1,1,1],[0,1,0]]
target = 5
# matrix = [[1,-1],[-1,1]]
# target = 0
matrix = [[904]]
target = 0
s = Solution()
print(s.numSubmatrixSumTarget(matrix, target))


# @lc code=end

