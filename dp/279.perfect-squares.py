#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

import math

class PerfectSquares:
    '''precomputation, O(n**1.5)
    '''
    def __init__(self):
        n = 10**4
        self.dp = [float('inf')] * (n + 1)
        self.dp[0] = 0
        ub = int(math.sqrt(n))
        coins = sorted([i ** 2 for i in range(1, ub + 1)], reverse=True)
        for coin in coins:
            for i in range(coin, n + 1):
                self.dp[i] = min(self.dp[i], self.dp[i - coin] + 1)


# @lc code=start
class Solution:
    perfect_squares = PerfectSquares()

    def numSquares(self, n: int) -> int:
        return Solution.perfect_squares.dp[n]



class Solution:
    '''iteratively deepening DFS
       There is a theorem called Lagrange's four-square theorem that states 
       every natural number can be represeted as the sum of four integer squares.
       So, the answer to the problem is upper bounded by 4
    '''
    def numSquares(self, n: int) -> int:

        def dfs(n, d) -> bool:
            if d == 1:
                if n in squarenum_set:
                    return True
                else:
                    return False
            for num in squarenum_list:
                if dfs(n - num, d - 1):
                    return True

        squarenum_set = set([i**2 for i in range(1, int(math.sqrt(n)) + 1)])
        squarenum_list = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
        depth = [1, 2, 3]
        for d in depth:
            if dfs(n, d):
                return d

        return 4
        



n = 12
s = Solution()
print(s.numSquares(n))

# @lc code=end

