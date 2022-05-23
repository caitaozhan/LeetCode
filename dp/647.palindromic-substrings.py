#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    '''dp1[i][j] is 1 if s[i...j] is palindrom
       dp2[i][j] is the number of palindrom substrings within s[i...j]
    '''
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # step 1: fill up dp1
        dp1 = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp1[i][i] = 1
        for i in range(n-1):
            if s[i] == s[i + 1]:
                dp1[i][i+1] = 1
        for length in range(2, n):
            for i in range(n-length):
                j = i + length
                if dp1[i+1][j-1] == 1 and s[i] == s[j]:
                    dp1[i][j] = 1
        
        # step 2: fill up dp2
        dp2 = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp2[i][i] = 1
        for length in range(1, n):
            for i in range(n-length):
                j = i + length
                dp2[i][j] = dp2[i][j-1] + dp2[i+1][j] - dp2[i+1][j-1] + dp1[i][j]
        
        return dp2[0][n-1]

s = "aaabc"
so = Solution()
print(so.countSubstrings(s))

# @lc code=end

