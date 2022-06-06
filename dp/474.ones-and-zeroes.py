#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

from typing import List
from copy import deepcopy

# @lc code=start
class Solution:
    '''two dimensional knapsack, i.e., there are two weights
       the value of each item is 1
       subproblem: dp[k][i][j] is the size of largest subset with i zeros and j ones when using the 1st to kth item
    '''
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        for k in range(1, len(strs)+1):
            s = strs[k-1]
            zero = s.count('0')
            one = s.count('1')
            for i in range(m + 1):
                for j in range(n + 1):
                    if i - zero >= 0 and j - one >= 0:
                        dp[k][i][j] = max(dp[k - 1][i][j], dp[k - 1][i - zero][j - one] + 1)
                    else:
                        dp[k][i][j] = dp[k-1][i][j]
        return dp[len(strs)][m][n]


class Solution:
    '''two dimensional knapsack, i.e., there are two weights
       the value of each item is 1
       subproblem: dp[i][j] is the size of largest subset with i zeros and j ones while iteration to the current item
       reducing space complexity
       O(len(strs) * m * n)
    '''
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp_pre = [[0]*(n + 1) for _ in range(m + 1)]
        for s in strs:
            dp = [[0]*(n + 1) for _ in range(m + 1)]
            zero = s.count('0')
            one = s.count('1')
            for i in range(m + 1):
                for j in range(n + 1):
                    if i - zero >= 0 and j - one >= 0:
                        dp[i][j] = max(dp_pre[i][j], dp_pre[i - zero][j - one] + 1)
                    else:
                        dp[i][j] = dp_pre[i][j]
            dp_pre = dp
        return dp[m][n]


class Solution:
    '''time complexity same as O(len(strs) * m * n), but runtime is faster
       trick: avoid using two dp arrays. use one dp array and when updating, go from end to start
              when going from start to end, you modify the earlier subproblems and it will affect the latter subproblems
              going from end to start will avoid this problem
    '''
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp= [[0]*(n + 1) for _ in range(m + 1)]
        for s in strs:
            zero = s.count('0')
            one = s.count('1')
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)
        return dp[m][n]


strs = ["10","0001","111001","1","0"]
m = 5
n = 3

# strs = ["10","0","1"]
# m = 1
# n = 1

# strs = ["1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101"]
# print(len(strs))
# m = 100
# n = 100
s = Solution()
print(s.findMaxForm(strs, m, n))

# @lc code=end
