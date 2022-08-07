#
# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
#

# @lc code=start
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        mydict = {'a': ['e', 'i', 'u'],
                  'e': ['a', 'i'],
                  'i': ['e', 'o'],
                  'o': ['i'],
                  'u': ['i', 'o']}
        dp     = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        dp_new = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        for _ in range(2, n + 1):
            for ch in ['a', 'e', 'i', 'o', 'u']:
                dp_new[ch] = (sum(dp[prev] for prev in mydict[ch])) % MOD
            dp, dp_new = dp_new, dp

        ans = 0
        for _, val in dp.items():
            ans += val
        return ans % MOD

n = 3
s = Solution()
print(s.countVowelPermutation(n))

# @lc code=end

