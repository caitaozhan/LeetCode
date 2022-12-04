'''

You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

Note:

The absolute difference of two numbers is the absolute value of their difference.
The average of n elements is the sum of the n elements divided (integer division) by n.
The average of 0 elements is considered to be 0.

'''

from typing import List
from itertools import accumulate

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix_sum = list(accumulate(nums))
        suffix_sum = list(accumulate(reversed(nums)))
        minn = float('inf')
        ans = -1
        n = len(nums)
        for i in range(n):
            left = int(prefix_sum[i] / (i + 1))
            if i < n - 1:
                right = int(suffix_sum[n - 2 - i] / (n - 1 - i))
            else:
                right = 0
            if abs(left - right) < minn:
                minn = abs(left - right)
                ans = i
        return ans
        
nums = [2,5,3,9,5,3]
s = Solution()
print(s.minimumAverageDifference(nums))