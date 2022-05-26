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


class Solution:
    '''dp1[i][j] is 1 if s[i...j] is palindrom
       no need for dp2, just count the number of 1 in dp1
    '''
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            ans += 1
        for i in range(n-1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = 1
                ans += 1
        for length in range(2, n):
            for i in range(n-length):
                j = i + length
                if dp[i+1][j-1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    ans += 1
        return ans


class Solution:
    '''expand around center method, no dp array needed
    '''
    def countSubstrings(self, s: str) -> int:
        
        def expand(s, left, right):
            count = 0
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                count += 1
                left -= 1
                right += 1
            return count

        ans = 0
        for i in range(len(s)):
            ans += expand(s, i, i)
            ans += expand(s, i, i+1)
        return ans




s = "aaabc"
so = Solution()
print(so.countSubstrings(s))

# @lc code=end

