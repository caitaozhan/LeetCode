#
# @lc app=leetcode id=1770 lang=python3
#
# [1770] Maximum Score from Performing Multiplication Operations
#

from typing import List

# @lc code=start
class Solution:
    '''dp[i][j] is the maximum value of using i number of elements in multipliers 
                and j number of elements in the left of nums, j <= i
    '''
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(m + 1):
                if j > i:
                    break
                if j == 0:
                    dp[i][j] = dp[i-1][j] + multipliers[i-1] * nums[n-i+j]   # picking the nums's right end
                elif i == j:
                    dp[i][j] = dp[i-1][j-1] + multipliers[i-1] * nums[j-1]     # picking the nums's left end
                else:
                    dp[i][j] = max(dp[i-1][j-1] + multipliers[i-1] * nums[j-1],    # picking the nums's left end
                                   dp[i-1][j]   + multipliers[i-1] * nums[n-i+j])  # picking the nums's right end
        return max(dp[m])


class Solution:
    '''dp[i][j] is the maximum value of using i number of elements in multipliers 
                and j number of elements in the left of nums, j <= i
       optimizing the space complexity
    '''
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp1 = [0] * (m + 1)
        dp2 = [0] * (m + 1)
        for i in range(1, m + 1):
            for j in range(m + 1):
                if j > i:
                    break
                if j == 0:
                    dp2[j] = dp1[j] + multipliers[i-1] * nums[n-i+j]   # picking the nums's right end
                elif i == j:
                    dp2[j] = dp1[j-1] + multipliers[i-1] * nums[j-1]     # picking the nums's left end
                else:
                    dp2[j] = max(dp1[j-1] + multipliers[i-1] * nums[j-1],    # picking the nums's left end
                                 dp1[j]   + multipliers[i-1] * nums[n-i+j])  # picking the nums's right end
            dp1, dp2 = dp2, dp1
        return max(dp1)


nums = [-5,-3,-3,-2,7,1]
multipliers = [-10,-5,3,4,6]
s = Solution()
print(s.maximumScore(nums, multipliers))

# @lc code=end

