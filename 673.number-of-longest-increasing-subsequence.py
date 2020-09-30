#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

'''
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

'''

from typing import List

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp1 = [1]*len(nums)
        dp2 = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp1[i] = max(dp1[i], dp1[j] + 1)
            if dp1[i] == 1:
                continue
            summ = 0
            for j in range(i):
                if dp1[j] == dp1[i] - 1:
                    summ += dp2[j]
            dp2[i] = summ

        maxx = max(dp1)
        summ = 0
        for i in range(len(dp2)):
            if dp1[i] == maxx:
                summ += dp2[i]
        print(dp1)
        print(dp2)
        return summ

# nums = [1,3,5,4,7]
# nums = [2,2,2,2,2]
nums = [1,3,5,4,7,6,1,2,4,6,1,9,4]
s = Solution()
print(s.findNumberOfLIS(nums))

# @lc code=end

