#
# @lc app=leetcode id=1641 lang=python3
#
# [1641] Count Sorted Vowel Strings
#

# @lc code=start
class Solution:
    '''backtrack
    '''
    def __init__(self):
        self.ans = 0

    def countVowelStrings(self, n: int) -> int:
        
        def backtrack(num, index):
            if index == n:
                self.ans += 1
                return
            
            for i in range(num, 6):
                backtrack(i, index+1)

        backtrack(num=1, index=0)
        return self.ans


class Solution:
    '''dp1
    subproblem: dp[i, v] is the number of legal strings for charecter v being at index i. v={0,1,2,3,4}, represents the {a,e,i,o,u}
    equation:   dp[i, v] = dp[i-1, v] + dp[i-1, v+1] + ... + dp[i-1, 4]
    answer:     sum(dp[n-1, :])
    '''
    def countVowelStrings(self, n: int) -> int:
        dp = [[0 for _ in range(5)] for _ in range(n)]
        for v in range(5):
            dp[0][v] = 1

        for i in range(1, n):
            for v in range(5):
                for j in range(v, 5):
                    dp[i][v] += dp[i-1][j]

        return sum(dp[n-1])


class Solution:
    '''dp2, this dp is less obvious than the dp1
    subproblem: dp[i, v] is the number of legal strings for using v number of vowels in a string of length i
    equation:   dp[i, v] = dp[i-1, v] + dp[i, v-1]. 
                           dp[i-1, v]: when you add 'a' at the beginning, the new string is always legal
                           dp[i, v-1]: when you use are allowed to use one more extra letter, you can just "add 1" to the charecters: 'a' to 'e', 'e' to 'i', etc. 
                                       After this change, the new string won't contain 'a'
    answer:     dp[n, 5]
    '''
    def countVowelStrings(self, n: int) -> int:
        dp = [[0 for _ in range(6)] for _ in range(n+1)]
        for num in range(1, 6):
            dp[1][num] = num
        
        for i in range(2, n + 1):
            dp[i][1] = 1
            for v in range(2, 6):
                dp[i][v] = dp[i - 1][v] + dp[i][v - 1]

        return dp[n][5]
    
class Solution:
    '''math... it is called combinations with repetition, link: https://en.wikipedia.org/wiki/Combination#Number_of_combinations_with_repetition
    '''
    def countVowelStrings(self, n: int) -> int:
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24
        


n = 4
s = Solution()
print(s.countVowelStrings(n))

# @lc code=end

