#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    '''DP
       input:      x[1...m], y[1...n], z[1...m+n]
       subproblem: dp[i][j] is 1 if x[1...i] and y[1...j] can interleave z[1...i+j]
       equation:   dp[i][j] = 1 if 1) dp[i-1][j] == 1 and x[i] == z[i+j]
                                   2) dp[i][j-1] == 1 and y[j] == z[i+j]
       answer:     dp[m][n]
       NOTE: the |n - m| <= 1 constraint will always be satisfied, it equals to the difference in number of "turn down" and "turn right" in the dp matrix
    '''
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def x(i):
            return s1[i-1]
        
        def y(j):
            return s2[j-1]
        
        def z(k):
            return s3[k-1]

        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for j in range(1, n+1):
            if dp[0][j-1] == 1 and y(j) == z(j):
                dp[0][j] = 1
            else:
                break

        for i in range(1, m+1):
            if dp[i-1][0] == 1 and x(i) == z(i):
                dp[i][0] = 1
            else:
                break
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if dp[i-1][j] == 1 and x(i) == z(i+j):
                    dp[i][j] = 1
                if dp[i][j-1] == 1 and y(j) == z(i+j):
                    dp[i][j] = 1
        
        return dp[m][n]


class Solution:
    '''DP
       O(n) space version
    '''
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def x(i):
            return s1[i-1]
        
        def y(j):
            return s2[j-1]
        
        def z(k):
            return s3[k-1]

        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False

        dp = [0] * (n + 1)
        dp[0] = 1
        for j in range(1, n+1):
            if dp[j-1] == 1 and y(j) == z(j):
                dp[j] = 1
            else:
                break

        dp_new = [0] * (n + 1)

        for i in range(1, m+1):
            if dp[0] == 1 and x(i) == z(i):
                dp_new[0] = 1

            for j in range(1, n+1):
                if (dp[j] == 1 and x(i) == z(i+j)) or (dp_new[j-1] == 1 and y(j) == z(i+j)):
                    dp_new[j] = 1
                else:
                    dp_new[j] = 0
            dp = dp_new
        
        return dp[n]


s1 = "aabcc"
s2 = "dbbca"
s3 = "adbabcabcc"

s1 = "db"
s2 = "b"
s3 = "cbb"

s1 = "aabd"
s2 = "abdc"
s3 = "aabdbadc"

s = Solution()
print(s.isInterleave(s1, s2, s3))


# @lc code=end

