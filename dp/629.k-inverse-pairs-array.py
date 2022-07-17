#
# @lc app=leetcode id=629 lang=python3
#
# [629] K Inverse Pairs Array
#

from itertools import accumulate

# @lc code=start
class Solution:
    '''dp
       O(nk) time and O(nk) space
    '''
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(1, n+1):                    # initialization
            dp[i][0] = 1
        for i in range(2, n+1):
            prefixsum = list(accumulate(dp[i-1]))  # prefix sum of subproblems
            max_j = min((i-1)*i//2, k)
            for j in range(1, max_j+1):
                lower = max(0, j-(i-1))
                if lower == 0:
                    dp[i][j] = prefixsum[j]
                else:  # lower >= 1
                    dp[i][j] = prefixsum[j] - prefixsum[lower-1]
        return dp[n][k] % (10**9 + 7)


class Solution:
    '''dp
       O(nk) time and O(k) space
       because of doing prefix sum on dp (saved dp's information), don't need a second dp
    '''
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [0] * (k+1)
        dp[0] = 1
        for i in range(2, n+1):
            prefixsum = list(accumulate(dp))  # prefix sum of subproblems
            max_j = min((i-1)*i//2, k)
            for j in range(1, max_j+1):
                lower = max(0, j-(i-1))
                if lower == 0:
                    dp[j] = prefixsum[j]
                else:  # lower >= 1
                    dp[j] = prefixsum[j] - prefixsum[lower-1]
        return dp[k] % (10**9 + 7)

n = 4
k = 6
s = Solution()
print(s.kInversePairs(n, k))
        
# @lc code=end

