#
# @lc app=leetcode id=823 lang=python3
#
# [823] Binary Trees With Factors
#

from typing import List

# @lc code=start
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        dp = {}
        arr.sort()
        for i, num in enumerate(arr):
            dp[num] = 1
            pairs = []    # find all num = a*b
            for j in range(i):
                if arr[j] ** 2 > num:
                    break
                if num % arr[j] == 0:
                    other = num // arr[j]
                    if other in dp:
                        pairs.append((arr[j], other))
            for a, b in pairs:
                if a == b:
                    dp[num] += dp[a] * dp[b]
                else:
                    dp[num] += 2 * dp[a] * dp[b]
            dp[num] = dp[num] % MOD
        return sum(dp.values()) % MOD


arr = [2, 4, 5, 10, 20]
s = Solution()
print(s.numFactoredBinaryTrees(arr))

        
# @lc code=end

